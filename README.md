# 게시판 REST API
## 실행 방법
	git clone https://github.com/Garo-o/wanted.git

	cd wanted/crud
	flask run
	
## 개발 환경
+ Language: Python 3.9
+ Framework: Flask
+ DataBase: SQLITE3

## 구현 방법
	 인증, 인가를 위해 jwt를 사용하였으며, role을 jwt claim에 넣어 역할별 사용할 수 있는 기능을 달리 했습니다.
	 rest end point는 flask_restful에 있는 Api의 add_resource()를 통해 클라스별로 구분하여 구현하였습니다.
	

## 도메인
+ *USER*
<pre>
<code>
{"id": integer, "email": string ,"password": string}
</code>
</pre>
+ *BOARD*
<pre>
<code>
{"id": integer, "title": string, "context": string, "writer": string, "regdate": string, "hit": integer}
</code>
</pre>

## API
### baseURL: "http://localhost:5000"
### user
+ __/auth/login__
<pre>
<code>
로그인
POST
request : {"email": string, "password": string}
response : {"result": string, "token": string}

예시
request : {"email": "admin", "password": "admin"}
response : {"result": "success", "token": xxxxx.yyyyy.zzzzz}
</code>
</pre>

+ __/auth/logout__
<pre>
<code>
로그아웃
POST
Header: {Authorization: "Bearer token"}

request : {}
response : {"result": string}

예시
request : {}
response : {"result": "success"}
</code>
</pre>

+ __/user__
<pre>
<code>
회원가입
POST
request : {"email": string, "password": string}
response : {"result": string}

예시
request : {"email": "hong@naver.com", "password": "123456"}
response : {"result": "success"}


전체 회원 조회 (관리자만 가능)
GET
Header: {Authorization: "Bearer token"}
request: {}
response: {"result": string, "count": integer, "data": list of user}

예시
request: {}
response: {"result": "success", "count": 3, "data": [
			{"id": 1, "email": "admin", "roles": ["ROLE_USER","ROLE_ADMIN"]},
			{"id": 2, "email": "admin2", "roles": ["ROLE_USER","ROLE_ADMIN"]},		
			{"id": 3, "email": "hong@naver.com", "roles": ["ROLE_USER"]}
			]}
</code>
</pre>

+ __/user/{param}__
<pre>
<code>
param = user_id

회원 삭제 (본인과 관리자만 가능)
DELETE 
Header: {Authorization: "Bearer token"}
request : {}
response : {"result": string}

예시
request : {}
response : {"result": "success"}

단일 회원 조회 (본인과 관리자만 가능)
GET
Header: {Authorization: "Bearer token"}
request : {}
response : {"result": string, "data": user}

예시
request : {}
response : {"result": "success", "data": {"id": 1, "email": "admin", "roles": ["ROLE_USER","ROLE_ADMIN"]}}
</code>
</pre>

+ __/user/update__
<pre>
<code>
회원 수정 (본인만 가능)
POST
Header: {Authorization: "Bearer token"}
request : {"password": string}
response : {"result": string}

예시
request : {"password": "as123"}
response : {"result": "success"}
</code>
</pre>

### BOARD
+ __/board__
<pre>
<code>
게시글 작성 (회원만 가능)
POST
Header: {Authorization: "Bearer token"}
request : {"title": string, "context": string}
response : {"result": string, "data": board}

예시
request : {"title": "제목", "context": "내용"}
response : {"result": "success", "data": {"id": 1,"title": "제목", "context": "내용", "writer": "admin", "regdate": "2021-10-27 01:12:23", "hit": 0}}


전체 목록 조회
GET
request : {}
response : {"result": string, "count": int, "data": list of board}

예시
request : {}
response : {"result": "success", "count": 2, "data": [
			{"id": 1,"title": "제목", "writer": "admin", "regdate": "2021-10-27 12:34:56", "hit": 4},
			{"id": 2,"title": "제목2", "writer": "admin2", "regdate": "2021-10-27 34:56:78", "hit": 0}
			]}
</code>
</pre>

+ __/board/{param}__
<pre>
<code>
param = board_id or offset

게시글 삭제 (본인과 관리자만 가능)
DELETE
Header: {Authorization: "Bearer token"}
request : {}
response : {"result": string}

예시
request : {}
response : {"result": "success"}


목록 조회 (offset-1)*limit번째부터 limit개의 게시글, limit = 5
GET
request : {}
response : {"result": string, "count": int, "data": list of board}

예시
request : {}
response : {"result": "success", "count": 5, "data": [
			{"id": 4,"title": "제목", "writer": "admin", "regdate": "2021-10-27 12:34:56", "hit": 4},
			{"id": 7,"title": "제목2", "writer": "admin2", "regdate": "2021-10-27 34:56:78", "hit": 0}
			...
			]}
			

게시글 수정 (본인만 가능)
POST
Header: {Authorization: "Bearer token"}
request : {"title": string, "context": string}
response : {"result": string, "data": board}

예시
request : {"title": "new board", "context": "asdasd"}
response : {"result": "success", "data": {"id": 4,"title": "new board", "context": "asdasd", "writer": "admin", "regdate": "2021-10-27 12:34:56", "hit": 4}}
</code>
</pre>


+ __/board/get/{param}__
<pre>
<code>
param = board_id

게시글 조회
GET
request : {}
response : {"result": string, "data":  board}

예시
request : {}
response : {"result": "success", "data": {"id": 4,"title": "제목", "context": "내용", "writer": "admin", "regdate": "2021-10-27 12:34:56", "hit": 4}}
</code>
</pre>


