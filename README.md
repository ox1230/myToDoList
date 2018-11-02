# myToDoList
for winter coding

version
python - 3.6
Django - 2.1.0
bootstrap - 3.3.7
jQuery - 3.3.1

#test 설명
integration test: integration_test.py
unit test: mylists.tests.py


#기능 설명
페이지는 root 하나로 구성된다.
root 페이지는 todo 입력- (아직 완료 안한) 할일 목록- 완료한 할일 목록으로 구성된다.

todo입력에서는 새로운 todo를 입력한다. text(내용), due(기한)은 입력하지 않을 수 있고, 
priority(우선도)는 디폴트로 1(보통)을 갖고, 2(중요),3(매우 중요)를 선택할 수 있다.

목록에서는 버튼 선택을 통해 todo를 완료처리하거나, 수정하거나, 삭제할 수 있다.
수정 버튼을 클릭할 시 바로 밑에 수정을 위한 row가 뜬다. 수정버튼을 다시 누르거나 위쪽 화살표 버튼을 눌러 row를 없앨 수 있다.
수정 후 저장 버튼을 누르면 todo값이 수정된다.
만약 기한이 오늘 날짜보다 전이라면( 완료 기한을 초과했다면), 그 todo의 row는 빨갛게 변하며, 마우스를 가져가면 기한이 지났다고 알려준다.

완료한 할일 목록에서는 버튼 선택을 통해 todo를 다시 완료 안했다고 처리하거나, 삭제할 수 있다.
