from database import Database
from teacher_crud import TeacherCRUD

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://100.24.20.161:7687", "neo4j", "indications-discoveries-metals")

# Criando uma instância da classe TeacherCRUD para interagir com o banco de dados
teacher_db = TeacherCRUD(db)

# Criando professor
teacher_db.create("Chris Lima", 1956, "182.052.396-66")

# Pesquisando professor
print(teacher_db.read("Chris Lima"))

# Atualizando o cpf do professor
teacher_db.update("Chris Lima", "162.052.777-77")


# Fechando a conexão
db.close()
