from pydantic import BaseModel
class ProdutoBase(BaseModel):
    nome: str
    preco: float
    quantidade: int


class Tabelapets(Pets):
    nome: str
    preco: float
    quantidade: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int
    
class Config:
    from_attributes = True