const cors = require('cors');
const express = require('express');
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

const app = express();
app.use(express.json());
app.use(cors({
    origin: 'http://127.0.0.1:5500', 
    methods: ['POST', 'GET'],
    allowedHeaders: ['Content-Type']
}));

mongoose.connect('mongodb+srv://syprayt:12312355Ss@a.wnwk8xk.mongodb.net/')
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.log('Failed to connect to MongoDB', err));


    // Define the user schema
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    mountain: { 
        type: [
            {
                image: { type: String, required: true },
                days: { type: Number, required: true },
                date: { type: Date, required: true}
            }
        ],
        default: []
    },
    character: {
        type: [
            {
                hair: { type: String, required: true },
                shirt: { type: String, required: true },
                pants: { type: String, required: true },
                skin: { type: String, required: true },
                shoes: { type: String, required: true },
                accessories: { type: String, required: true },
            }
        ],
        default: []
    }

});
const User = mongoose.model('User', userSchema);

app.post('/register', async (req, res) => {
    const { username, email, password } = req.body;

    if (!username || !email || !password) {
        return res.status(400).json({ error: "All fields are required" });
    }
    else{
        const existingUser = await User.findOne({ $or: [{ username }, { email }] });
        if (existingUser) {
            let errorMessage = '';
            if (existingUser.username === username) {
                errorMessage = 'The username is already taken'
            }
            if (existingUser.email === email) {
                errorMessage = 'The email is already registered';
            }
            return res.status(400).json({ error: errorMessage });
        }
        else{

            try {
                const hashedPassword = await bcrypt.hash(password, 10);
        
                const newUser = new User({
                    username: username,
                    password: hashedPassword,
                    email: email,
                });
        
                await newUser.save();
                console.log('User saved');
                res.status(200).json({ message: 'User registered successfully' });
            } catch (err) {
                console.log('Error saving user', err);
                res.status(500).json({ error: 'Registration failed' });
            }
        }
        }
        
});

app.post('/login', async (req, res) => {
    const { email, password } = req.body;
    
    if (!email || !password) {
        return res.status(400).json({ error: "Email and password are required" });
    }

    try {
        const user = await User.findOne({ email });
        if (!user) {
            return res.status(401).json({ error: "Invalid username or password" });
        }

        const passwordMatch = await bcrypt.compare(password, user.password);
        if (!passwordMatch) {
            return res.status(401).json({ error: "Invalid email or password" });
        }

        res.status(200).json({ message: "Login successful" });
    } catch (err) {
        console.log('Login error', err);
        res.status(500).json({ error: "Login failed" });
    }
});
app.post(‘/mountain’, async(req, res) => {
    const { username } = req.body;
    if(!username) {
        return res.status(400).json({ error: "User is not founded" });
    try {
        const user = await User.findOne( {username} );
        if (!user) {
            return res.status(401).json({ error: "User is not founded" });
        }
        const style = user. mountain
        res.json( { reply: style } );

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});