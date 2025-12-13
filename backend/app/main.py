from fastapi import FastAPI

from dotenv import load_dotenv

from fastapi.middleware.cors import CORSMiddleware

class App(FastAPI):
    def __init__(self):
        super().__init__(
            title="Ambalance Backend",
            description="Backend API for Ambalance application",
            version="1.0.0",
        )
        load_dotenv()
        # Middleware
        self.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        # Event handlers
        self.add_event_handler("startup", self.startup_event)
        self.add_event_handler("shutdown", self.shutdown_event)

    async def startup_event(self):
        print("Starting up...")

    async def shutdown_event(self):
        print("Shutting down...")

app = App()