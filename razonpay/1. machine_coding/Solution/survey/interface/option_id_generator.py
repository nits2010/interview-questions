from interface.id_generator import IdGenerator
import uuid


class OptionIdGenerator(IdGenerator):

    def generate_id(self) -> str:
        return str(uuid.uuid4())