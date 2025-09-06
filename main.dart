import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

// Clase principal de la aplicación
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false, // 👈 Quita el banner DEBUG
      title: 'Contador Flutter',
      theme: ThemeData(
        primarySwatch: Colors.green,
        scaffoldBackgroundColor: const Color.fromARGB(255, 144, 168, 137), // 👈 color de fondo
      ),
      home: const MyHomePage(),
    );
  }
}

// Clase para la página principal
class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;
  String _mensaje = "";

  void _incrementCounter() {
    setState(() {
      if (_counter < 100) {
        _counter++;
        _mensaje = "";
      }
    });
  }

  void _decrementCounter() {
    setState(() {
      if (_counter > 0) {
        _counter--;
        _mensaje = "";
      } else {
        _mensaje = "⚠️ El contador no puede ser negativo";
      }
    });
  }

  void _resetCounter() {
    setState(() {
      _counter = 0;
      _mensaje = "";
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Mi Contador Personal'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'Valor del contador:',
              style: TextStyle(fontSize: 20),
            ),
            Text(
              '$_counter',
              style: const TextStyle(
                fontSize: 50,
                fontWeight: FontWeight.bold,
                color: Colors.purple,
              ),
            ),
            const SizedBox(height: 20),

            // Mensaje de advertencia
            if (_mensaje.isNotEmpty)
              Text(
                _mensaje,
                style: const TextStyle(color: Colors.red, fontSize: 16),
              ),

            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                  onPressed: _decrementCounter,
                  child: const Text('Disminuir'),
                ),
                const SizedBox(width: 30),
                ElevatedButton(
                  onPressed: _incrementCounter,
                  child: const Text('Incrementar'),
                ),
                const SizedBox(width: 30),
                ElevatedButton(
                  onPressed: _resetCounter,
                  child: const Text('Reiniciar'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
