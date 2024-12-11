<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller; 
use App\Models\PaisUrl;
use Illuminate\Http\Request;

class PaisController extends Controller
{
    /**
     * Obtener todos los países.
     */
    public function index()
    {
        $paises = PaisUrl::all();
        return response()->json([
            'success' => true,
            'data' => $paises,
        ], 200);
    }

    /**
     * Crear un nuevo país.
     */
    public function store(Request $request)
    {
        // Validamos los datos recibidos
        $validatedData = $request->validate([
            'iso' => 'required|string|max:2|unique:paises_url,iso',
            'name' => 'required|string|max:255',
        ]);

        // Creamos un nuevo país
        $pais = PaisUrl::create($validatedData);

        return response()->json([
            'success' => true,
            'message' => 'País creado con éxito',
            'data' => $pais,
        ], 201);
    }

    /**
     * Mostrar un país específico.
     */
    public function show($id)
    {
        try {
            $pais = PaisUrl::findOrFail($id);
            return response()->json([
                'success' => true,
                'data' => $pais,
            ], 200);
        } catch (\Exception $e) {
            return response()->json([
                'success' => false,
                'message' => 'País no encontrado',
            ], 404);
        }
    }

    /**
     * Actualizar un país.
     */
    public function update(Request $request, $id)
    {
        try {
            $pais = PaisUrl::findOrFail($id);

            // Validamos los datos recibidos
            $validatedData = $request->validate([
                'iso' => "required|string|max:2|unique:paises_url,iso,{$id}",
                'name' => 'required|string|max:255',
            ]);

            // Actualizamos el país
            $pais->update($validatedData);

            return response()->json([
                'success' => true,
                'message' => 'País actualizado con éxito',
                'data' => $pais,
            ], 200);
        } catch (\Exception $e) {
            return response()->json([
                'success' => false,
                'message' => 'País no encontrado o error en la actualización',
            ], 404);
        }
    }

    /**
     * Eliminar un país.
     */
    public function destroy($id)
    {
        try {
            $pais = PaisUrl::findOrFail($id);
            $pais->delete();

            return response()->json([
                'success' => true,
                'message' => 'País eliminado con éxito',
            ], 200);
        } catch (\Exception $e) {
            return response()->json([
                'success' => false,
                'message' => 'País no encontrado o error al eliminar',
            ], 404);
        }
    }
}
