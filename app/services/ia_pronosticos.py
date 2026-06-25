"""
Servicio de pronósticos con Inteligencia Artificial (Google Gemini).

Genera 3 pronósticos en texto a partir de los datos reales de cada
gráfica del sistema (ventas por mes, platos por categoría, top platos),
usando la API gratuita de Google Gemini.

Requiere la variable de entorno GEMINI_API_KEY (ver archivo .env en la
raíz del proyecto). Esa clave NUNCA debe subirse a GitHub.
"""
import os
import json

from google import genai
from google.genai import types

MODELO = "gemini-2.5-flash"


def _obtener_cliente():
    """Crea el cliente de Gemini usando la API key de la variable de
    entorno. Devuelve None si la key no está configurada, para que el
    resto del sistema pueda mostrar un mensaje claro en vez de fallar."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return None
    return genai.Client(api_key=api_key)


def generar_pronosticos(contexto: str, datos: dict) -> dict:
    """
    Pide a Gemini 3 pronósticos en español, en formato JSON, basados en
    los datos reales que se le pasan.

    Args:
        contexto: descripción breve de qué gráfica es (ej. "ventas
            mensuales del restaurante", "platos más vendidos por
            categoría", "top 5 platos más vendidos").
        datos: diccionario con los datos reales de la gráfica
            (ej. {"meses": [...], "montos": [...]}).

    Returns:
        dict con la forma {"ok": True, "pronosticos": [str, str, str]}
        o {"ok": False, "error": "mensaje"} si algo falla.
    """
    cliente = _obtener_cliente()
    if cliente is None:
        return {
            "ok": False,
            "error": (
                "No se configuró GEMINI_API_KEY. Agrega tu clave en el "
                "archivo .env en la raíz del proyecto."
            ),
        }

    prompt = f"""Eres un analista de negocios para un restaurante boliviano llamado "El Deseo".

Contexto de los datos: {contexto}

Datos reales del sistema (formato JSON):
{json.dumps(datos, ensure_ascii=False)}

Con base en estos datos reales, genera exactamente 3 pronósticos breves
y concretos sobre lo que podría pasar a futuro en este aspecto del
negocio. Cada pronóstico debe tener 1-2 oraciones, en español, con un
tono profesional y orientado a la toma de decisiones (no inventes
números exactos que no se puedan justificar con los datos dados; basa
el pronóstico en la tendencia visible).
"""

    try:
        respuesta = cliente.models.generate_content(
            model=MODELO,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.4,
                max_output_tokens=1024,
                response_mime_type="application/json",
                response_schema={
                    "type": "object",
                    "properties": {
                        "pronosticos": {
                            "type": "array",
                            "items": {"type": "string"},
                        }
                    },
                    "required": ["pronosticos"],
                },
            ),
        )
        texto = respuesta.text.strip()
        data = json.loads(texto)
        pronosticos = data.get("pronosticos", [])

        if not pronosticos:
            return {"ok": False, "error": "La IA no devolvió pronósticos."}

        return {"ok": True, "pronosticos": pronosticos[:3]}

    except Exception as exc:
        return {"ok": False, "error": f"Error al generar pronósticos: {exc}"}
