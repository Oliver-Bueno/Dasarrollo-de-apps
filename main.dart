import 'package:flutter/material.dart';

void main() => runApp(const ModernAppBarDemo());

class ModernAppBarDemo extends StatelessWidget {
  const ModernAppBarDemo({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'AppBar Personalizada',
      theme: ThemeData(
        scaffoldBackgroundColor: const Color(0xFFF6F8FA),
        appBarTheme: const AppBarTheme(
          backgroundColor: Color(0xFF002B5B), // Azul oscuro elegante
          foregroundColor: Colors.white, // Color del texto e íconos
          centerTitle: true, // Centra el título
          elevation: 4,
          titleTextStyle: TextStyle(
            fontSize: 22,
            fontWeight: FontWeight.bold,
            fontFamily: 'Roboto',
          ),
        ),
      ),
      home: const CustomAppBarPage(),
    );
  }
}

class CustomAppBarPage extends StatelessWidget {
  const CustomAppBarPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Image.network(
            'https://upload.wikimedia.org/wikipedia/commons/1/17/Google-flutter-logo.png',
            fit: BoxFit.contain,
          ),
        ),
        title: const Text('Mi Aplicación de tareas'),
        actions: [
          IconButton(
            icon: const Icon(Icons.notifications),
            tooltip: 'Notificaciones',
            onPressed: () {
              ScaffoldMessenger.of(context).showSnackBar(
                SnackBar(
                  content: const Text(
                    '¡Tienes nuevas tareas por completar!',
                    style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                  ),
                  backgroundColor: Colors.blueAccent,
                  duration: const Duration(seconds: 3),
                  behavior: SnackBarBehavior.floating,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(12),
                  ),
                ),
              );
            },
          ),
          IconButton(
            icon: const Icon(Icons.navigate_next),
            tooltip: 'Ir a siguiente página',
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (_) => const NextPage(),
                ),
              );
            },
          ),
        ],
      ),
      body: const Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.auto_awesome, color: Color(0xFF002B5B), size: 50),
            SizedBox(height: 20),
            Text(
              'Bienvenido a la Aplicación de tareas',
              style: TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
                color: Color(0xFF002B5B),
              ),
            ),
            SizedBox(height: 8),
            Text(
              'Interfaz moderna y profesional',
              style: TextStyle(
                fontSize: 16,
                color: Colors.black54,
                fontStyle: FontStyle.italic,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class NextPage extends StatelessWidget {
  const NextPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Siguiente Página'),
      ),
      body: const Center(
        child: Text(
          'Para mas funcionalidades 👨‍💻',
          style: TextStyle(fontSize: 20),
        ),
      ),
    );
  }
}
