# wanted

baseUrl: "http:localhost:5000"

API명세

USER
{"id": int, "email": string ,"password": string}

"/user"
post: 유저 등록
request: {"email": string, "password": string}
response: {"result": string}

get: 모든 유저 조회
request: {}
response: {"result": string, "count": int, "data": list of user}

"/user/<param>"
param: int
delete: param==id인 유저 삭제
request: {}
response: {"result": string}

get: param==id인 유저 조회
request: {}
response: {"result": string, "data": user}


"/user/update"
post: 유저 업데이트
request: {"password": string}
response: {"result": string}


BOARD
{"id": int, "title": string, "context": string, "writer": string, "regdate": string, "fixdate":string}


"/board"
post: 게시글 등록
request: {"title": string "context": string, "writer": string}
response: {"result": string}

get: 모든 게시글 조회
request: {} 
response: {"result": string, "count": int, "data": list of board}


"/board/<param>"
param: int
get: (param-1) x limit 에 해당하는 id부터 limit개의 게시글 조회, limit = 5로 서버에서 지정
request: {}
response: {"result": string, "count": int, "data": list of board}

delete: id==param인 게시글 삭제
request: {}
response: {"result": string}


"/board/update"
post: 게시글 업데이트
request: {"title": string "context": string}
response: {"result": string}


"/board/get/<param>"
get: param==id인 게시글 조회
request: {}
response: {"result": string, "data": board}
