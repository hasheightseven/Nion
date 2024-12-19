export const neonmain = document.createElement('div');


neonmain.textContent = 'nion!!';

neonmain.style.color = '#abcdef';

async function ello() {
  const colors = [ '#112692', '#261192', '#921126', '#abcdef' ]; 
  let currentColorIndex = 0;

    // Function to change color
    function changeColor() {
        // Set the text color to the next color in the array
        document.getElementById('neonmain').style.color = colors[currentColorIndex];

        // Move to the next color, and loop back to the first color when reaching the end
        currentColorIndex = (currentColorIndex + 1) % colors.length;
    }

    // Set an interval to change color every 5 seconds (5000ms)
    setInterval(changeColor, 5000);
}

ello()
