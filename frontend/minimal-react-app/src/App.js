import React from 'react';
import EventForm from './components/EventForm';
import EventList from './components/EventList';
import ToggleButton from './components/ToggleButton';

const App = () => {
    return (
        <div>
            <h1>Screen Monitor App</h1>
            <EventForm />
            <EventList />
            <ToggleButton />
        </div>
    );
};

export default App;