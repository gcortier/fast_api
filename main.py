from typing import Dict
from fastapi import FastAPI, HTTPException
from loguru import logger
from pydantic import BaseModel
app = FastAPI()


citations = {
    1: "La vie est un mystère qu'il faut vivre, et non un problème à résoudre.",
    2: "Le plus grand plaisir de la vie est l'amour.",
    3: "L'avenir appartient à ceux qui croient à la beauté de leurs rêves.",
}


@app.get("/")
async def root():
    logger.info("Route '/' appelée.")
    return {"message": "Hello World!"}


@app.get("/citations")
async def lire_citations():
    return citations


@app.get("/citation/{citation_id}")
async def lire_citation(citation_id: int) -> Dict[int, str]:
    logger.info(f"Route '/citation/{citation_id}' appelée.")
    if citation_id in citations:
        logger.debug(f"Citation trouvée : {citations[citation_id]}")
        return {citation_id: citations[citation_id]}
    else:
        logger.warning(f"Citation {citation_id} non trouvée.")
        raise HTTPException(status_code=404, detail="Citation non trouvée")
    


class Citation(BaseModel):
    citation: str

# add post method : 
@app.post("/citation/")
async def creer_citation(citation: Citation) -> Dict[str, str]:
    logger.info("Route '/citation/' (POST) appelée.")
    nouvel_id = max(citations.keys()) + 1 if citations else 0  # Trouver le prochain ID disponible
    citations[nouvel_id] = citation.citation
    logger.debug(f"Citation ajoutée : {citation.citation}")
    return {"message": f"Citation ajoutée avec l'ID {nouvel_id}"}


# add put method :
@app.put("/citation/{citation_id}")
async def modifier_citation(citation_id: int, citation: Citation) -> Dict[str, str]:
    logger.info(f"Route '/citation/{citation_id}' (PUT) appelée.")
    if citation_id in citations:
        citations[citation_id] = citation.citation
        logger.debug(f"Citation modifiée : {citation.citation}")
        return {"message": f"Citation {citation_id} modifiée"}
    else:
        logger.warning(f"Citation {citation_id} non trouvée pour modification.")
        raise HTTPException(status_code=404, detail="Citation non trouvée")
    
    
    
# add delete method :
@app.delete("/citation/{citation_id}")
async def supprimer_citation(citation_id: int) -> Dict[str, str]:
    logger.info(f"Route '/citation/{citation_id}' (DELETE) appelée.")
    if citation_id in citations:
        del citations[citation_id]
        logger.debug(f"Citation {citation_id} supprimée.")
        return {"message": f"Citation {citation_id} supprimée"}
    else:
        logger.warning(f"Citation {citation_id} non trouvée pour suppression.")
        raise HTTPException(status_code=404, detail="Citation non trouvée")