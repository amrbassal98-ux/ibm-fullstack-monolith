import express from 'express';

const router = express.Router();

router.post('/', (req, res) => {
    const newTask = req.body;
    if (newTask && newTask !== null) {
        console.log("Received Task:", newTask);
        res.status(201).json({message: "Task stored", data: newTask});
    };
});

export default router;