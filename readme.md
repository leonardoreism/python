API, REST e RESTFUL


# API -> HTTP
Acrônimo de "Application Programming Interface" (Interface de Programação de Aplicações) -> é uma aplicação formando um conjunto de rotinas, para que outras aplicações possam usar essas aplicações feitas pela API.

# REST
Acrônimo de "Representational State Transfer" (Trasnferência de Estado Representativo)
Determina algumas obrigaçãoes nessa transferência de dados feita por uma API. -> Usando HTTP.

# 6 constraints para ser RESTFUL

# RESTFUL

1 - _Client-server_: separar cliente de servidor. Desta forma, teremos uma portabilidade do sistema. Posso fazer requisições dentro de um APP utilizando uma API que ele fornece.

2 - _Stateless_: sem estado. No literal: "menos estado". Toda requisição que for feita para o servidor, precisa ser completa, com todas as informações, para o servidor entender e responder a requisição corretamente. (response / request).
*ex: Se um usuário faz uma requisição em uma API, na próxima requisição, ele deve ser autenticado novamente. O servidor não pode ter armazenado essa primeira autenticação do usuário, uma nova autenticação deve ser feita após toda nova requisição.

3 - _Cacheable_: As respostas das requisições deverão ser explicitas ao dizer se aquela requisição pode ou não ser cacheada pelo cliente.

4 - _Layered System_: O cliente acessa o endpoint sem ter conhecimento da complexidade que está sendo executada internamente no servidor para retornar ao cliente o que foi pedido.

5 - _Code on demand_(optional): O servidor (backend) envia ao cliente um script para o cliente rodar no frontend.

Restful -> aplicar os padrões REST.