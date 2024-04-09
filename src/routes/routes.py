from src.controllers.controller import *


routes = {
    "index_route": "/", "index_route_controller": IndexController.as_view("index"),
    "binarioSM_route": "/binarioParaSM", "binarioSM_route_controller": BinaryToSmController.as_view("binarioParaSM"),
    "binarioCTWO_route": "/binarioParaComplementoDois", "binarioCTWO_route_controller": BinaryToCTwoController.as_view("binarioParaComplementoDois"),
    "decimalBinary_route": "/decimalParaBinario", "decimalBinary_route_controller": DecimalToBinaryController.as_view("decimalParaBinario"),
    "decimalBinaryCTWO_route": "/decimalParaBinarioComplementoDois", "decimalBinaryCTWO_route_controller": DecimalToBinaryCTwoController.as_view("decimalParaBinarioComplementoDois"),
    "decimalBinarySM_route": "/decimalParaBinarioSinalMagnitude", "decimalBinarySM_route_controller": DecimalToBinarySmController.as_view("decimalParaBinarioSinalMagnitude"),
    "binaryFixedPointFractionalDecimal_route": "/binarioPontoFixoParaDecimalFracionario", "binaryFixedPointFractionalDecimal_route_controller": BinaryFixedPointToFracinalDecimalController.as_view("binaryFixedPointFractionalDecimal"),
}