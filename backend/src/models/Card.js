import mongoose from "mongoose"

// create schema
const cardSchema = new mongoose.Schema(
    {
        jp_word: {
            type: String,
            required: true
        },
        jp_reading: {
            type: String,
            required: true
        },
        jp_meanings: { // string with clear seperater for multiple meanings
            type: String,
            required: true
        }
    },
    { timestamps: true } // createdAt, updatedAt
);

// model based on schema
const Card = mongoose.model("Card", cardSchema)

export default Card