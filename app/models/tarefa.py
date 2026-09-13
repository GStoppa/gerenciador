#Tarefa (cls)
class Tarefa:
    def __init__(self, id_tarefa, descricao, estado):
        self.id_tarefa = id_tarefa
        self.descricao = descricao
        self.estado = estado

    def alternar_status(self):
        self.estado = not self.estado

    def para_dict(self):
        return {
            "id_tarefa": self.id_tarefa,
            "descricao": self.descricao,
            "estado": self.estado,
        }

    #vai receber toda a classe (e não só um self especifico)
    @classmethod
    def from_dict(cls, dados):
        #cls é mesma coisa que Tarefa(...)
        return cls(
            id_tarefa=dados["id_tarefa"],
            descricao=dados["descricao"],
            estado=dados.get("estado", False)
        )