function startRecognition(fieldId) {
    if (!('webkitSpeechRecognition' in window)) {
        alert('Your browser does not support speech recognition.');
        return;
    }

    var recognition = new webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onstart = function() {
        console.log('Voice recognition started. Speak into the microphone.');
    };

    recognition.onresult = function(event) {
        var result = event.results[0][0].transcript;
        document.getElementById(fieldId).value = result;
        console.log('Voice recognition result: ', result);
    };

    recognition.onerror = function(event) {
        console.error('Voice recognition error: ', event.error);
    };

    recognition.onend = function() {
        console.log('Voice recognition ended.');
    };

    recognition.start();
}
