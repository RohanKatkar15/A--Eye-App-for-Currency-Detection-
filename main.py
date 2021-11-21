import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:path/path.dart';
// import 'package:path_provider/path_provider.dart';
// import 'package:torch_compat/torch_compat.dart';
// import 'package:flutter_tts/flutter_tts.dart';
// import 'package:tflite/tflite.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final cameras = await availableCameras();
  final firstCamera = cameras.first;
  runApp(MaterialApp(
    theme: ThemeData.dark(),
    debugShowCheckedModeBanner: false,
    home: Picture(
      firstCamera,
    ),
  ));
}

class Picture extends StatefulWidget {
  final CameraDescription camera;
  Picture(this.camera);

  @override
  _PictureState createState() => _PictureState();
}

class _PictureState extends State<Picture> {
  late CameraController _controller;
  late Future<void> _initializeControllerFuture;

  @override
  void initState() {
    super.initState();
    _controller = CameraController(
      widget.camera,
      ResolutionPreset.high,
    );
    _initializeControllerFuture = _controller.initialize();
  }

  @override
  void dispose() {
    // _controller?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Center(child: Text('A EYE'))),
      body: FutureBuilder<void>(
        future: _initializeControllerFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.done) {
            return CameraPreview(_controller);
          } else {
            return Center(child: CircularProgressIndicator());
          }
        },
      ),
      floatingActionButton: Column(
        mainAxisAlignment: MainAxisAlignment.end,
        children: <Widget>[
          Center(
            child: Container(
              height: 180.0,
              width: 200.0,
              child: FittedBox(
                child: FloatingActionButton(
                  child: Icon(Icons.camera_alt),
                  // Provide an onPressed callback.
                  onPressed: () {},
                  mini: true,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
