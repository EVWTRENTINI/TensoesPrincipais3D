import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# Definição do tensor de tensão
tensor = np.array([[-30.,   40.,    0.],
                   [ 40.,   50.,  -50.],
                   [  0.,  -50.,  -50.]])

# Cálculo das tensões principais e dos eixos principais
tensoes_principais, eixos_principais = np.linalg.eig(tensor)


print(tensoes_principais)
print("")
print(eixos_principais)


# Preparação do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Coordenadas do centro do gráfico
x_center, y_center, z_center = 0, 0, 0

# Definindo o cubo
# Vértices do cubo
vertices = np.array([[-1, -1, -1],
                     [1, -1, -1],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, 1],
                     [1, -1, 1],
                     [1, 1, 1],
                     [-1, 1, 1]])

# Escala o cubo para ser pequeno no centro
scale = 30
vertices = vertices * scale

# Aplica a rotação para alinhar o cubo com os eixos principais
rotation_matrix = eixos_principais
rotated_vertices = vertices.dot(np.transpose(rotation_matrix))

# Cria as faces do cubo rotacionado
faces = [[rotated_vertices[i] for i in [0, 1, 2, 3]],
         [rotated_vertices[i] for i in [4, 5, 6, 7]], 
         [rotated_vertices[i] for i in [0, 3, 7, 4]], 
         [rotated_vertices[i] for i in [1, 2, 6, 5]], 
         [rotated_vertices[i] for i in [0, 1, 5, 4]], 
         [rotated_vertices[i] for i in [2, 3, 7, 6]]]

# Desenhar o cubo
cubo = Poly3DCollection(faces, facecolors='gray', linewidths=1, edgecolors='black', alpha=.5)
ax.add_collection3d(cubo)


# Desenhar os eixos principais com pares de vetores representando as tensões
cores = ['r', 'g', 'b']
legendas = []
for i in range(3):
    eixo = eixos_principais[:, i]
    tensao = tensoes_principais[i]


    if tensao > 0:
    	# Vetor positivo
    	ax.quiver(x_center+eixo[0]*scale , y_center+eixo[1]*scale, z_center+eixo[2]*scale, tensao * eixo[0], tensao * eixo[1], tensao * eixo[2], color=cores[i], linewidths=2)
	
    	# Vetor negativo (oposto)
    	ax.quiver(x_center-eixo[0]*scale , y_center-eixo[1]*scale , z_center-eixo[2]*scale , -tensao * eixo[0], -tensao * eixo[1], -tensao * eixo[2], color=cores[i], linewidths=2)
    else:
    	# Vetor positivo
    	ax.quiver(x_center+tensao * eixo[0]-eixo[0]*scale, y_center+tensao * eixo[1]-eixo[1]*scale, z_center+tensao * eixo[2]-eixo[2]*scale, -tensao * eixo[0], -tensao * eixo[1], -tensao * eixo[2], color=cores[i], linewidths=2)
	
    	# Vetor negativo (oposto)
    	ax.quiver(x_center-tensao * eixo[0]+eixo[0]*scale, y_center-tensao * eixo[1]+eixo[1]*scale, z_center-tensao * eixo[2]+eixo[2]*scale, +tensao * eixo[0], +tensao * eixo[1], +tensao * eixo[2], color=cores[i], linewidths=2)
    
    # Adiciona uma legenda para cada tensão principal
    legenda = f'Tensão {i+1}: {tensao:.2f}'
    legendas.append(legenda)
    # Cria linhas de exemplo para a legenda
    linhas = [plt.Line2D([0], [0], color=cor, linewidth=3) for cor in cores]

    # Adiciona a legenda ao gráfico
    ax.legend(linhas, legendas, loc='upper right')



    



# Configurações do gráfico
ax.set_xlim([-150, 150])
ax.set_ylim([-150, 150])
ax.set_zlim([-150, 150])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Elemento rotacionado e Tensões Principais')
#ax.axis('off')
ax.set_box_aspect([1, 1, 1])

plt.show()

