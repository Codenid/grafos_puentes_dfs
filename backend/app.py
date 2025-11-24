from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import GraphRequest, BridgeResponse
from graph import Graph
from bridge_finder import BridgeFinder

app = FastAPI(title="Detección de Puentes (DFS)")

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # si quieres, puedes restringir a ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/bridges", response_model=BridgeResponse)
def detect_bridges(data: GraphRequest):
    # Construir grafo
    g = Graph(data.nodes)
    for u, v in data.edges:
        g.add_edge(u, v)

    # Encontrar puentes
    finder = BridgeFinder(g)
    bridges = finder.get_bridges()

    return {"bridges": bridges}
