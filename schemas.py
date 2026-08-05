# schemas.py
<<<<<<< HEAD

from pydantic import BaseModel
=======
from pydantic import BaseModel

>>>>>>> 14d06886dc54d91a5e1442d089da045973f50cfe
class ProdutoBase(BaseModel):
    nome: str
    preco: float
    quantidade: int
class ProdutoCreate(ProdutoBase):
    pass
class ProdutoResponse(ProdutoBase):
    id: int
<<<<<<< HEAD

=======
>>>>>>> 14d06886dc54d91a5e1442d089da045973f50cfe
class Config:
    from_attributes = True