from interface.id_generator import IdGenerator
import uuid


class QuestionIdGenerator(IdGenerator):

    def generate_id(self) -> str:
        return str(uuid.uuid4())
