const express = require('express');
const multer = require('multer');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(express.static('public'));

app.post('/upload', upload.single('photo'), (req, res) => {
    try {
        const filePath = req.file.path;
        
        exec(`python analyze.py ${filePath}`, (error, stdout, stderr) => {
            fs.unlinkSync(filePath); // アップロード画像を削除
            console.log(error)
            if (error) {
                return res.status(500).json({ error: 'Error processing image' });
            }
            res.json({ emotion: stdout.trim() });
        });
    } catch (error) {
        res.status(500).json({ error: 'Error processing image' });
    }
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));
