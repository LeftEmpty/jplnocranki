import express from "express"
import dotenv from "dotenv"
import cardsRoutes from "./routes/cardsRoutes.js"
import { connectDB } from "./config/db.js"

const app = express();
const PORT = process.env.PORT || 3333 // fallback

dotenv.config();

connectDB()

app.use("api/notes", cardsRoutes)

app.listen(PORT, () => {
    console.log("Server started on PORT: " + PORT);
});
