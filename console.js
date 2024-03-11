const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

// Sample data - replace this with your own database
let items = [];

// GET all items
app.get('/api/items', (req, res) => {
    res.json(items);
});

// GET single item
app.get('/api/items/:id', (req, res) => {
    const id = req.params.id;
    const item = items.find(item => item.id === parseInt(id));
    if (!item) return res.status(404).json({ message: 'Item not found' });
    res.json(item);
});

// POST new item
app.post('/api/items', (req, res) => {
    const item = req.body;
    items.push(item);
    res.status(201).json(item);
});

// PUT update item
app.put('/api/items/:id', (req, res) => {
    const id = req.params.id;
    const updatedItem = req.body;
    const index = items.findIndex(item => item.id === parseInt(id));
    if (index === -1) return res.status(404).json({ message: 'Item not found' });
    items[index] = { ...items[index], ...updatedItem };
    res.json(items[index]);
});

// DELETE item
app.delete('/api/items/:id', (req, res) => {
    const id = req.params.id;
    const index = items.findIndex(item => item.id === parseInt(id));
    if (index === -1) return res.status(404).json({ message: 'Item not found' });
    const deletedItem = items.splice(index, 1);
    res.json(deletedItem[0]);
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
