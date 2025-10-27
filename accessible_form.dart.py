import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../widgets/accessible_button.dart';
import '../utils/accessibility_utils.dart';

class AccessibleFormScreen extends StatefulWidget {
  const AccessibleFormScreen({super.key});

  @override
  State<AccessibleFormScreen> createState() => _AccessibleFormScreenState();
}

class _AccessibleFormScreenState extends State<AccessibleFormScreen> {
  final _formKey = GlobalKey<FormState>();
  final _nameController = TextEditingController();
  final _emailController = TextEditingController();
  final _phoneController = TextEditingController();

  bool _isLoading = false;
  bool _highContrast = false;
  double _fontSize = 16.0;

  @override
  void dispose() {
    _nameController.dispose();
    _emailController.dispose();
    _phoneController.dispose();
    super.dispose();
  }

  void _submitForm() async {
    if (_formKey.currentState!.validate()) {
      setState(() => _isLoading = true);
      HapticFeedback.mediumImpact();

      await Future.delayed(const Duration(seconds: 2));

      if (mounted) {
        setState(() => _isLoading = false);
        AccessibilityUtils.showAccessibleSnackBar(
          context,
          'Formulario enviado correctamente',
        );
      }
    }
  }

  void _increaseFontSize() {
    setState(() {
      _fontSize += 2.0;
      if (_fontSize > 24.0) _fontSize = 24.0;
    });
  }

  void _decreaseFontSize() {
    setState(() {
      _fontSize -= 2.0;
      if (_fontSize < 14.0) _fontSize = 14.0;
    });
  }

  @override
  Widget build(BuildContext context) {
    // 🎨 Definición de colores según el modo
    final backgroundGradient = _highContrast
        ? [const Color(0xFF001F3F), const Color(0xFF003C8F)] // Fondo oscuro-azul intenso
        : [const Color(0xFFE3F2FD), const Color(0xFFBBDEFB)]; // Fondo claro

    final cardColor =
        _highContrast ? const Color(0xFF004BA0) : const Color(0xFFFFFFFF);

    final textColor = _highContrast ? Colors.white : Colors.black87;
    final inputBorderColor = _highContrast ? Colors.white70 : Colors.grey;
    final primaryColor =
        _highContrast ? Colors.lightBlueAccent : Colors.blueAccent;

    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: backgroundGradient,
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: SafeArea(
          child: Column(
            children: [
              AppBar(
                backgroundColor: Colors.transparent,
                elevation: 0,
                title: Semantics(
                  header: true,
                  child: const Text('Formulario Accesible'),
                ),
                actions: [
                  IconButton(
                    onPressed: _increaseFontSize,
                    icon: const Icon(Icons.zoom_in),
                    tooltip: 'Aumentar tamaño de texto',
                  ),
                  IconButton(
                    onPressed: _decreaseFontSize,
                    icon: const Icon(Icons.zoom_out),
                    tooltip: 'Disminuir tamaño de texto',
                  ),
                  Semantics(
                    label: 'Activar o desactivar modo alto contraste',
                    toggled: _highContrast,
                    child: Switch(
                      activeColor: Colors.white,
                      inactiveThumbColor: Colors.blueAccent,
                      value: _highContrast,
                      onChanged: (value) {
                        setState(() => _highContrast = value);
                        AccessibilityUtils.showAccessibleSnackBar(
                          context,
                          value
                              ? 'Modo azul oscuro activado'
                              : 'Modo claro activado',
                        );
                      },
                    ),
                  ),
                ],
              ),
              Expanded(
                child: SingleChildScrollView(
                  padding: const EdgeInsets.all(16),
                  child: Form(
                    key: _formKey,
                    child: Semantics(
                      container: true,
                      child: FocusTraversalGroup(
                        policy: OrderedTraversalPolicy(),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.stretch,
                          children: [
                            Semantics(
                              header: true,
                              child: Text(
                                'Complete sus datos',
                                style: TextStyle(
                                  fontSize: 24,
                                  fontWeight: FontWeight.bold,
                                  color: textColor,
                                ),
                              ),
                            ),
                            const SizedBox(height: 24),

                            _buildAccessibleField(
                              label: 'Nombre Completo',
                              hint: 'Ingrese su nombre y apellido',
                              icon: Icons.person,
                              controller: _nameController,
                              borderColor: inputBorderColor,
                              textColor: textColor,
                              validator: (value) => value == null || value.isEmpty
                                  ? 'Por favor ingrese su nombre'
                                  : null,
                            ),

                            const SizedBox(height: 16),

                            _buildAccessibleField(
                              label: 'Correo Electrónico',
                              hint: 'ejemplo@correo.com',
                              icon: Icons.email,
                              controller: _emailController,
                              borderColor: inputBorderColor,
                              textColor: textColor,
                              keyboardType: TextInputType.emailAddress,
                              validator: (value) {
                                if (value == null || value.isEmpty) {
                                  return 'Por favor ingrese su email';
                                }
                                if (!RegExp(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$')
                                    .hasMatch(value)) {
                                  return 'Ingrese un email válido';
                                }
                                return null;
                              },
                            ),

                            const SizedBox(height: 16),

                            _buildAccessibleField(
                              label: 'Teléfono',
                              hint: '+1234567890',
                              icon: Icons.phone,
                              controller: _phoneController,
                              borderColor: inputBorderColor,
                              textColor: textColor,
                              keyboardType: TextInputType.phone,
                              validator: (value) => value == null || value.isEmpty
                                  ? 'Por favor ingrese su teléfono'
                                  : null,
                            ),

                            const SizedBox(height: 32),

                            FocusVisible(
                              child: AccessibleButton(
                                onPressed: _isLoading ? null : _submitForm,
                                text: _isLoading ? 'Enviando...' : 'Enviar Formulario',
                                icon: _isLoading ? Icons.hourglass_top : Icons.send,
                                backgroundColor: primaryColor,
                                textColor: _highContrast ? Colors.black : Colors.white,
                                fontSize: _fontSize,
                              ),
                            ),

                            const SizedBox(height: 16),

                            Semantics(
                              container: true,
                              label:
                                  'Información de accesibilidad. Esta aplicación incluye características para usuarios con discapacidades visuales y motoras.',
                              child: Card(
                                color: cardColor,
                                elevation: 4,
                                child: Padding(
                                  padding: const EdgeInsets.all(16),
                                  child: Column(
                                    crossAxisAlignment: CrossAxisAlignment.start,
                                    children: [
                                      Text(
                                        'Características Accesibles:',
                                        style: TextStyle(
                                          fontSize: _fontSize,
                                          fontWeight: FontWeight.bold,
                                          color: primaryColor,
                                        ),
                                      ),
                                      const SizedBox(height: 8),
                                      _buildFeatureItem('✓ Tamaño de texto ajustable'),
                                      _buildFeatureItem('✓ Navegación por voz compatible'),
                                      _buildFeatureItem('✓ Alto contraste disponible'),
                                      _buildFeatureItem('✓ Etiquetas descriptivas'),
                                    ],
                                  ),
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),

      floatingActionButton: FocusVisible(
        child: Semantics(
          button: true,
          label: 'Limpiar formulario',
          child: FloatingActionButton(
            onPressed: () {
              HapticFeedback.mediumImpact();
              _nameController.clear();
              _emailController.clear();
              _phoneController.clear();
              AccessibilityUtils.showAccessibleSnackBar(
                context,
                'Formulario limpiado',
              );
            },
            tooltip: 'Limpiar formulario',
            backgroundColor: Colors.orangeAccent,
            child: const Icon(Icons.cleaning_services),
          ),
        ),
      ),
    );
  }

  Widget _buildAccessibleField({
    required String label,
    required String hint,
    required IconData icon,
    required TextEditingController controller,
    required Color borderColor,
    required Color textColor,
    required String? Function(String?) validator,
    TextInputType? keyboardType,
  }) {
    return Semantics(
      textField: true,
      label: label,
      hint: hint,
      value: controller.text.isEmpty ? null : controller.text,
      child: FocusVisible(
        child: TextFormField(
          controller: controller,
          keyboardType: keyboardType,
          decoration: InputDecoration(
            labelText: label,
            hintText: hint,
            prefixIcon: Icon(icon, color: textColor),
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(8),
              borderSide: BorderSide(color: borderColor),
            ),
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(8),
              borderSide: BorderSide(color: borderColor),
            ),
            labelStyle: TextStyle(color: textColor),
            hintStyle: TextStyle(color: textColor.withOpacity(0.7)),
          ),
          style: TextStyle(fontSize: _fontSize, color: textColor),
          validator: validator,
        ),
      ),
    );
  }

  Widget _buildFeatureItem(String text) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Text(
        text,
        style: TextStyle(fontSize: _fontSize - 2, color: Colors.black87),
      ),
    );
  }
}

class FocusVisible extends StatelessWidget {
  final Widget child;
  const FocusVisible({super.key, required this.child});

  @override
  Widget build(BuildContext context) {
    return Focus(
      child: Builder(
        builder: (context) {
          final hasFocus = Focus.of(context).hasFocus;
          return AnimatedContainer(
            duration: const Duration(milliseconds: 150),
            decoration: BoxDecoration(
              border: hasFocus
                  ? Border.all(color: Colors.blueAccent, width: 2)
                  : null,
              borderRadius: BorderRadius.circular(8),
            ),
            child: child,
          );
        },
      ),
    );
  }
}