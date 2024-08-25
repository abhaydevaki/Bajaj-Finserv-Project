function submitData() {
    const data = document.getElementById('json-input').value;
    const errorMessage = document.getElementById('error-message');
    const dropdownContainer = document.getElementById('dropdown-container');
    const responseContainer = document.getElementById('response');

    try {
        const jsonData = JSON.parse(data);
        fetch('/bfhl', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonData)
        })
        .then(response => response.json())
        .then(data => {
            errorMessage.textContent = '';
            dropdownContainer.classList.remove('hidden');
            responseContainer.textContent = JSON.stringify(data, null, 2);
            localStorage.setItem('responseData', JSON.stringify(data));
        })
        .catch(error => {
            console.error('Error:', error);
            errorMessage.textContent = 'An error occurred while processing your request.';
        });
    } catch (e) {
        errorMessage.textContent = 'Invalid JSON format. Please correct it and try again.';
    }
}

function displaySelectedData() {
    const selectedOptions = Array.from(document.getElementById('data-select').selectedOptions).map(option => option.value);
    const responseContainer = document.getElementById('response');
    const data = JSON.parse(localStorage.getItem('responseData'));

    const filteredData = {};
    selectedOptions.forEach(option => {
        filteredData[option] = data[option];
    });

    responseContainer.textContent = JSON.stringify(filteredData, null, 2);
}
