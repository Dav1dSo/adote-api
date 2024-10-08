from src.controllers.interfaces.person_create_controller import PersonCreateControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PersonCreateView(ViewInterface):
    def __init__(self, controller: PersonCreateControllerInterface) -> None:
        self.__controller = controller
        
    
    def handle(self, http_request: HttpRequest) -> HttpRequest:
        person_info = http_request.body
        body_response = self.__controller.create.create(person_info)
        
        return HttpResponse(status_code=201, body=body_response)