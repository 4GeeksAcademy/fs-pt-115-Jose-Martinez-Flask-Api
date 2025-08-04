from flask import Flask, jsonify, request

# iniciar flask
app = Flask(__name__)

# variable global + "db" la he cambiado a false para testear
todos = [
    { "done": True, "label": "Sacar al perro." },
    { "done": False, "label": "Comprar el pan" }
]

# Endpoint para OBTENER todas las tareas 
@app.route('/todos', methods=['GET'])
def get_todos():
    # devolver la lista en formato JSON
    return jsonify(todos)

# Endpoint para AÑADIR una nueva tarea
@app.route('/todos', methods=['POST'])
def add_new_todo():
    # Hago 'todos' global para poder reasignarla
    global todos
    # para obtener el cuerpo de la nueva tarea
    request_body = request.json
    print("Recibiendo nueva tarea...", request_body)
    
    # para añadir la tarea a nuestra lista 'todos' usando concatenación
    todos = todos + [request_body]
    
    # devuelve la lista actualizada
    return jsonify(todos)

# Endpoint para ELIMINAR una tarea
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("Eliminando tarea en la posición:", position)

    # si la posición es válida para evitar errores
    if position >= len(todos) or position < 0:
        return "Posición fuera de rango", 400
        
    # elemento de la lista en la posición indicada usando 'del'
    del todos[position]
    
    # me deuvelve la lista actualizada
    return jsonify(todos)

# iniciar el servidor 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)