import React, { useState } from 'react';
import './ToggleButton.css';

const ToggleButton = () => {
    const [isToggled, setIsToggled] = useState(false);

    const handleToggle = () => {
        setIsToggled(!isToggled);
    };

    return (
        <button
            className={`toggle-button ${isToggled ? 'green' : 'red'}`}
            onClick={handleToggle}
        >
            {isToggled ? 'Toggled' : 'Not Toggled'}
        </button>
    );
};

export default ToggleButton;