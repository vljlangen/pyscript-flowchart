# FlowchartWizard Web

A simple web application that generates beautiful flowcharts from sequential text input. Built with PyScript, it runs entirely in the browser without requiring a server.

## Features

- 🎯 **Simple Input**: Just type your steps separated by double newlines
- 🎨 **Auto-sized Flowcharts**: Charts automatically adjust to content
- 🔗 **Clean Arrows**: Properly positioned arrows that don't overlap with text
- 📱 **Web-based**: Runs entirely in the browser using PyScript
- 🎨 **Professional Look**: Clean, square nodes with proper spacing

## How to Use

1. Open `index.html` in your web browser
2. Enter your flowchart steps in the textarea, separating each step with a double newline (press Enter twice)
3. Click "Draw Flowchart" to generate your visual flowchart

### Example Input:
```
Start
Initialize variables

Process data
Validate input

End
```

## Technical Details

- **Frontend**: HTML, CSS, PyScript
- **Backend**: Python (runs in browser)
- **Libraries**: Matplotlib, NetworkX
- **Rendering**: Client-side Python execution

## File Structure

```
flowchart/
├── index.html          # Main web interface
├── main.py            # Python logic for flowchart generation
├── pyscript.toml      # PyScript configuration
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Requirements

- Modern web browser with JavaScript enabled
- Internet connection (for PyScript CDN)

## How It Works

1. User inputs text steps in the web interface
2. PyScript loads Python code in the browser
3. Python code uses NetworkX to create a directed graph
4. Matplotlib renders the flowchart with proper arrow positioning
5. The chart is displayed in the browser

## Customization

You can modify the appearance by adjusting these parameters in `main.py`:

- `arrow_offset`: Controls how close arrows get to nodes
- `v_step`: Vertical spacing between nodes
- `fontsize`: Text size in nodes
- `pad`: Padding inside nodes

## License

This project is open source and available under the MIT License.
