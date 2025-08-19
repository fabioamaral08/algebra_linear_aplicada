#!/usr/bin/env python3
"""
Exercícios Extras - Introdução ao Python para Álgebra Linear
Aula 1: Vetores, Operações e Conceitos Fundamentais

Este arquivo contém exercícios adicionais para praticar os conceitos
apresentados na aula.
"""

import numpy as np
import matplotlib.pyplot as plt

def teste_conceitos_basicos():
    """Testa os conceitos básicos de vetores"""
    print("=== TESTE: Conceitos Básicos ===")
    
    # Criando vetores
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    
    # Operações básicas
    soma = v1 + v2
    produto_escalar = 2 * v1
    produto_interno = np.dot(v1, v2)
    norma_v1 = np.linalg.norm(v1)
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {soma}")
    print(f"2 * v1 = {produto_escalar}")
    print(f"v1 · v2 = {produto_interno}")
    print(f"||v1|| = {norma_v1:.3f}")
    
    # Verificações
    assert np.array_equal(soma, np.array([5, 7, 9])), "Erro na soma"
    assert np.array_equal(produto_escalar, np.array([2, 4, 6])), "Erro na multiplicação por escalar"
    assert produto_interno == 32, "Erro no produto interno"
    assert np.isclose(norma_v1, np.sqrt(14)), "Erro na norma"
    
    print("✓ Todos os testes passaram!")
    print()

def exercicio_aplicacao_fisica():
    """Exercício de aplicação em física"""
    print("=== EXERCÍCIO: Aplicação em Física ===")
    print("Um objeto se move no espaço 3D com as seguintes informações:")
    
    # Dados do problema
    posicao_inicial = np.array([2, 1, 0])  # metros
    velocidade = np.array([3, -1, 2])      # m/s
    tempo = 5                              # segundos
    
    print(f"Posição inicial: {posicao_inicial} m")
    print(f"Velocidade: {velocidade} m/s")
    print(f"Tempo: {tempo} s")
    
    # a) Calcule a posição final
    deslocamento = velocidade * tempo
    posicao_final = posicao_inicial + deslocamento
    
    print(f"\na) Deslocamento: {deslocamento} m")
    print(f"   Posição final: {posicao_final} m")
    
    # b) Calcule a distância percorrida
    distancia_percorrida = np.linalg.norm(deslocamento)
    print(f"\nb) Distância percorrida: {distancia_percorrida:.3f} m")
    
    # c) Calcule a velocidade escalar (módulo da velocidade)
    velocidade_escalar = np.linalg.norm(velocidade)
    print(f"\nc) Velocidade escalar: {velocidade_escalar:.3f} m/s")
    
    # d) Calcule a distância da origem na posição final
    distancia_origem = np.linalg.norm(posicao_final)
    print(f"\nd) Distância da origem na posição final: {distancia_origem:.3f} m")
    
    print()

def exercicio_economia():
    """Exercício de aplicação em economia"""
    print("=== EXERCÍCIO: Aplicação em Economia ===")
    print("Uma empresa produz 4 tipos de produtos com os seguintes dados:")
    
    # Dados do problema
    produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D']
    custos_producao = np.array([15.00, 22.50, 8.75, 31.20])  # custo por unidade
    precos_venda = np.array([25.00, 35.00, 15.00, 50.00])    # preço por unidade
    producao_mensal = np.array([1200, 800, 2000, 500])       # unidades produzidas
    
    print("Dados dos produtos:")
    for i, produto in enumerate(produtos):
        print(f"{produto}: Custo R${custos_producao[i]:.2f}, Preço R${precos_venda[i]:.2f}, Produção {producao_mensal[i]} unidades")
    
    # a) Calcule o custo total de produção
    custo_total = np.dot(custos_producao, producao_mensal)
    print(f"\na) Custo total de produção: R$ {custo_total:,.2f}")
    
    # b) Calcule a receita total
    receita_total = np.dot(precos_venda, producao_mensal)
    print(f"b) Receita total: R$ {receita_total:,.2f}")
    
    # c) Calcule o lucro total
    lucro_por_unidade = precos_venda - custos_producao
    lucro_total = np.dot(lucro_por_unidade, producao_mensal)
    print(f"c) Lucro total: R$ {lucro_total:,.2f}")
    
    # d) Calcule a margem de lucro por produto
    margem_lucro = (lucro_por_unidade / precos_venda) * 100
    print(f"\nd) Margem de lucro por produto:")
    for i, produto in enumerate(produtos):
        print(f"   {produto}: {margem_lucro[i]:.1f}%")
    
    # e) Identifique o produto mais lucrativo
    produto_mais_lucrativo = np.argmax(lucro_por_unidade * producao_mensal)
    print(f"\ne) Produto mais lucrativo: {produtos[produto_mais_lucrativo]}")
    
    print()

def exercicio_geometria_avancado():
    """Exercício avançado de geometria"""
    print("=== EXERCÍCIO: Geometria Avançada ===")
    print("Análise de um quadrilátero no plano:")
    
    # Vértices do quadrilátero
    A = np.array([0, 0])
    B = np.array([4, 0])
    C = np.array([5, 3])
    D = np.array([1, 3])
    
    vertices = [A, B, C, D]
    nomes = ['A', 'B', 'C', 'D']
    
    print("Vértices:")
    for i, nome in enumerate(nomes):
        print(f"{nome} = {vertices[i]}")
    
    # a) Calcule os vetores dos lados
    lados = []
    nomes_lados = ['AB', 'BC', 'CD', 'DA']
    
    lados.append(B - A)  # AB
    lados.append(C - B)  # BC
    lados.append(D - C)  # CD
    lados.append(A - D)  # DA
    
    print(f"\na) Vetores dos lados:")
    for i, nome_lado in enumerate(nomes_lados):
        print(f"{nome_lado} = {lados[i]}")
    
    # b) Calcule o perímetro
    comprimentos = [np.linalg.norm(lado) for lado in lados]
    perimetro = sum(comprimentos)
    
    print(f"\nb) Comprimentos dos lados:")
    for i, nome_lado in enumerate(nomes_lados):
        print(f"|{nome_lado}| = {comprimentos[i]:.3f}")
    print(f"Perímetro = {perimetro:.3f}")
    
    # c) Calcule as diagonais
    AC = C - A
    BD = D - B
    
    print(f"\nc) Diagonais:")
    print(f"AC = {AC}, |AC| = {np.linalg.norm(AC):.3f}")
    print(f"BD = {BD}, |BD| = {np.linalg.norm(BD):.3f}")
    
    # d) Verifique se as diagonais são perpendiculares
    produto_diagonais = np.dot(AC, BD)
    print(f"\nd) Produto interno das diagonais: {produto_diagonais}")
    if abs(produto_diagonais) < 1e-10:
        print("   As diagonais são perpendiculares!")
    else:
        print("   As diagonais não são perpendiculares.")
    
    # e) Calcule a área usando produto vetorial (em 2D)
    # Área = |AB × AD| / 2 (usando determinante)
    AB = B - A
    AD = D - A
    area = abs(AB[0] * AD[1] - AB[1] * AD[0]) / 2
    print(f"\ne) Área do quadrilátero: {area:.3f}")
    
    # f) Visualize o quadrilátero
    plt.figure(figsize=(8, 6))
    
    # Plotando o quadrilátero
    vertices_plot = np.array([A, B, C, D, A])  # fechando o polígono
    plt.plot(vertices_plot[:, 0], vertices_plot[:, 1], 'b-o', linewidth=2, markersize=8)
    
    # Plotando as diagonais
    plt.plot([A[0], C[0]], [A[1], C[1]], 'r--', linewidth=1, alpha=0.7, label='Diagonal AC')
    plt.plot([B[0], D[0]], [B[1], D[1]], 'g--', linewidth=1, alpha=0.7, label='Diagonal BD')
    
    # Anotando os vértices
    for i, nome in enumerate(nomes):
        plt.annotate(nome, vertices[i], xytext=(5, 5), textcoords='offset points', 
                    fontsize=12, fontweight='bold')
    
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Quadrilátero ABCD')
    plt.legend()
    plt.show()
    
    print()

def exercicio_ortogonalidade():
    """Exercício sobre ortogonalidade e projeções"""
    print("=== EXERCÍCIO: Ortogonalidade e Projeções ===")
    
    # Vetores dados
    u = np.array([3, 4])
    v = np.array([4, -3])
    w = np.array([1, 2])
    
    print(f"Vetores dados:")
    print(f"u = {u}")
    print(f"v = {v}")
    print(f"w = {w}")
    
    # a) Verifique quais pares são ortogonais
    print(f"\na) Verificando ortogonalidade:")
    uv = np.dot(u, v)
    uw = np.dot(u, w)
    vw = np.dot(v, w)
    
    print(f"u · v = {uv} → {'Ortogonais' if uv == 0 else 'Não ortogonais'}")
    print(f"u · w = {uw} → {'Ortogonais' if uw == 0 else 'Não ortogonais'}")
    print(f"v · w = {vw} → {'Ortogonais' if vw == 0 else 'Não ortogonais'}")
    
    # b) Calcule a projeção de w sobre u
    proj_w_u = (np.dot(w, u) / np.dot(u, u)) * u
    print(f"\nb) Projeção de w sobre u:")
    print(f"proj_u(w) = {proj_w_u}")
    print(f"|proj_u(w)| = {np.linalg.norm(proj_w_u):.3f}")
    
    # c) Calcule a componente de w perpendicular a u
    w_perp = w - proj_w_u
    print(f"\nc) Componente de w perpendicular a u:")
    print(f"w_perp = {w_perp}")
    
    # d) Verifique que w_perp é ortogonal a u
    produto_perp = np.dot(w_perp, u)
    print(f"\nd) Verificação de ortogonalidade:")
    print(f"w_perp · u = {produto_perp:.10f} ≈ 0? {abs(produto_perp) < 1e-10}")
    
    # e) Verifique que w = proj_u(w) + w_perp
    w_reconstruido = proj_w_u + w_perp
    print(f"\ne) Verificação da decomposição:")
    print(f"proj_u(w) + w_perp = {w_reconstruido}")
    print(f"w = {w}")
    print(f"São iguais? {np.allclose(w, w_reconstruido)}")
    
    # f) Visualize a projeção
    plt.figure(figsize=(8, 6))
    
    # Plotando os vetores
    plt.arrow(0, 0, u[0], u[1], head_width=0.1, head_length=0.1, 
              fc='blue', ec='blue', linewidth=2, label='u')
    plt.arrow(0, 0, w[0], w[1], head_width=0.1, head_length=0.1, 
              fc='red', ec='red', linewidth=2, label='w')
    plt.arrow(0, 0, proj_w_u[0], proj_w_u[1], head_width=0.1, head_length=0.1, 
              fc='green', ec='green', linewidth=2, label='proj_u(w)')
    plt.arrow(proj_w_u[0], proj_w_u[1], w_perp[0], w_perp[1], 
              head_width=0.1, head_length=0.1, fc='purple', ec='purple', 
              linewidth=2, label='w_perp')
    
    # Linha pontilhada da projeção
    plt.plot([w[0], proj_w_u[0]], [w[1], proj_w_u[1]], 'k--', alpha=0.5)
    
    plt.xlim(-1, 5)
    plt.ylim(-1, 3)
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Projeção de w sobre u')
    plt.legend()
    plt.axis('equal')
    plt.show()
    
    print()

def main():
    """Função principal que executa todos os exercícios"""
    print("EXERCÍCIOS EXTRAS - ÁLGEBRA LINEAR COM PYTHON")
    print("=" * 50)
    print()
    
    # Executando todos os exercícios
    teste_conceitos_basicos()
    exercicio_aplicacao_fisica()
    exercicio_economia()
    exercicio_geometria_avancado()
    exercicio_ortogonalidade()
    
    print("=" * 50)
    print("TODOS OS EXERCÍCIOS CONCLUÍDOS!")
    print("Continue praticando para dominar os conceitos de álgebra linear.")

if __name__ == "__main__":
    main()

