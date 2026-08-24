from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import ProdutoDB, PetsDB
from schemas import ProdutoCreate, ProdutoResponse, PetCreate, PetResponse

Base.metadata.create_all(bind=engine) # cria as tabelas, se ainda não existirem
app = FastAPI()
# Habilita CORS para permitir requisições do front-end (ajuste em produção)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/produtos', response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(ProdutoDB).all()

@app.post('/produtos', response_model=ProdutoResponse, status_code=201)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo_produto = ProdutoDB(**produto.dict())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto


@app.get('/produtos/{produto_id}', response_model=ProdutoResponse)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    return produto

@app.delete('/produtos/{produto_id}', status_code=204)
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    # remove o produto e confirma a transação
    db.delete(produto)
    db.commit()


# PUT 
@app.put('/produtos/{produto_id}', response_model=ProdutoResponse)
def atualizar_produto(produto_id: int, dados: ProdutoCreate, db:
Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')

    produto.nome = dados.nome
    produto.preco = dados.preco
    produto.quantidade = dados.quantidade
    db.commit()
    db.refresh(produto)
    return produto


# Rotas para pets
@app.get('/pets', response_model=list[PetResponse])
def listar_pets(db: Session = Depends(get_db)):
    return db.query(PetsDB).all()


@app.post('/pets', response_model=PetResponse, status_code=201)
def criar_pet(pet: PetCreate, db: Session = Depends(get_db)):
    novo_pet = PetsDB(**pet.dict())
    db.add(novo_pet)
    db.commit()
    db.refresh(novo_pet)
    return novo_pet


@app.get('/pets/{pet_id}', response_model=PetResponse)
def obter_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(PetsDB).filter(PetsDB.id == pet_id).first()
    if pet is None:
        raise HTTPException(status_code=404, detail='Pet não encontrado')
    return pet


@app.delete('/pets/{pet_id}', status_code=204)
def remover_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(PetsDB).filter(PetsDB.id == pet_id).first()
    if pet is None:
        raise HTTPException(status_code=404, detail='Pet não encontrado')
    db.delete(pet)
    db.commit()


@app.put('/pets/{pet_id}', response_model=PetResponse)
def atualizar_pet(pet_id: int, dados: PetCreate, db: Session = Depends(get_db)):
    pet = db.query(PetsDB).filter(PetsDB.id == pet_id).first()
    if pet is None:
        raise HTTPException(status_code=404, detail='Pet não encontrado')

    pet.nome = dados.nome
    pet.especie = dados.especie
    pet.raca = dados.raca
    pet.idade = dados.idade
    db.commit()
    db.refresh(pet)
    return pet