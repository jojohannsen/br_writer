from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from openai_functions_tool_retrieval_agent import agent_executor as openai_functions_tool_retrieval_agent_chain
from pirate_speak.chain import chain as pirate_speak_chain

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


add_routes(app, openai_functions_tool_retrieval_agent_chain, path="/openai-functions-tool-retrieval-agent")
add_routes(app, pirate_speak_chain, path="/pirate-speak")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
