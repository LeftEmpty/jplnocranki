export async function getAllCards (req, res) {
    res.status(200).send("Fetched all cards.");
}

export async function createCard (req, res) {
    res.status(201).json({ message: "card created successfully!" });
}

export async function updateCard (req, res) {
    res.status(200).json({ message: "card updated successfully!" });
}

export async function deleteCard (req, res) {
    res.status(200).json({ message: "card deleted successfully!" });
}