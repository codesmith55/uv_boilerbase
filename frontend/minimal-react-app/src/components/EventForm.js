import React, { useState } from 'react';
import axios from 'axios';

const EventForm = () => {
    const [location, setLocation] = useState('');
    const [type, setType] = useState('');
    const [typeDetails, setTypeDetails] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(`${process.env.REACT_APP_API_URL}/events`, {"location": location, "type": type, "typeDetails": typeDetails});
            console.log(response.data);
            // Optionally, you can reset the form fields here
        } catch (error) {
            console.error('Error adding event:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Location:</label>
                <input
                    type="text"
                    value={location}
                    onChange={(e) => setLocation(e.target.value)}
                    required
                />
            </div>
            <div>
                <label>Type:</label>
                <input
                    type="text"
                    value={type}
                    onChange={(e) => setType(e.target.value)}
                    required
                />
            </div>
            <div>
                <label>Type Details:</label>
                <input
                    type="text"
                    value={typeDetails}
                    onChange={(e) => setTypeDetails(e.target.value)}
                    required
                />
            </div>
            <button type="submit">Add Event</button>
        </form>
    );
};

export default EventForm;