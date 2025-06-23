import express from "express"
import { getAllCards, createCard, updateCard, deleteCard } from "../controllers/cardsController.js";


const router = express.Router();

router.get("/", getAllCards);
router.post("/", createCard);
router.put("/:id", updateCard);
router.delete("/:id", deleteCard);

export default router;
