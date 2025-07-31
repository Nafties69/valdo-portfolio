
let sceneObjects = [];
let selectedObjectType = 'fairy'; // Default object type

function setup() {
    const canvas = createCanvas(600, 400);
    canvas.parent('canvas-container'); // Attach canvas to a specific container
    background(240);
}

function draw() {
    background(240);
    for (const obj of sceneObjects) {
        drawObject(obj);
    }
}

function mousePressed() {
    // Only add an object if the mouse is within the canvas bounds
    if (mouseX > 0 && mouseX < width && mouseY > 0 && mouseY < height) {
        let newObj = {
            x: mouseX,
            y: mouseY,
            type: selectedObjectType,
            color: color(random(150, 255), random(150, 255), random(150, 255), 150),
            size: random(20, 50)
        };
        sceneObjects.push(newObj);
    }
}

function drawObject(obj) {
    fill(obj.color);
    noStroke();
    if (obj.type === 'fairy') {
        // Draw a simple circle for a fairy
        ellipse(obj.x, obj.y, obj.size, obj.size);
    } else if (obj.type === 'tree') {
        // Draw a simple rectangle and circle for a tree
        fill(139, 69, 19); // Brown for trunk
        rect(obj.x - obj.size / 4, obj.y, obj.size / 2, obj.size);
        fill(34, 139, 34); // Green for leaves
        ellipse(obj.x, obj.y, obj.size * 1.5, obj.size);
    }
}

function clearCanvas() {
    sceneObjects = [];
    background(240);
}

function aiEnhance() {
    // Simple "AI" effect: apply a tint to the whole canvas
    tint(255, 204, 0, 126); // Apply a yellowish tint
    image(get(), 0, 0);
    noTint();
}

function exportScene() {
    saveCanvas('fairy-scene', 'png');
}

// Functions to be called by HTML buttons
window.setObjectType = (type) => {
    selectedObjectType = type;
    console.log("Object type set to: " + type);
};

window.clearCanvas = clearCanvas;
window.aiEnhance = aiEnhance;
window.exportScene = exportScene;
