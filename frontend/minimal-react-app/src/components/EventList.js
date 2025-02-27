import React, { useEffect, useState } from 'react';
import axios from 'axios';

const EventList = () => {
    const [events, setEvents] = useState([]);

    useEffect(() => {
        const fetchEvents = async () => {
            try {
                const response = await axios.get(`${process.env.REACT_APP_API_URL}/events`);
                setEvents(response.data);
            } catch (error) {
                console.error('Error fetching events:', error);
            }
        };

        fetchEvents();
    }, []);

    return (
        <div>
            <h2>Event List</h2>
            <ul>
                {events.map((event) => (
                    <li key={event.id}>
                        {event.location} - {event.type} - {event.typeDetails}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default EventList;