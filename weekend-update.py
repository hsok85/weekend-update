from plankapy import *

if __name__ == "__main__":

    planka = Planka(
        "URL",
        "ID",
        "PW"
    )

    project    = Project(planka)
    board      = Board(planka)
    list       = List(planka)
    card       = Card(planka)
    label      = Label(planka)
    task       = Task(planka)
    attachment = Attachment(planka)
    stopwatch  = Stopwatch(planka)
    background = Background(planka)
    comment    = Comment(planka)
    user       = User(planka)

    for _project in project.get_project_names():

        print(_project)

        for _board in board.get(_project):

            print("")
            print("" + _board['name'])

            # 완료내역부터 BACKLOG 순서로 정렬
            reversedLists = reversed(list.get(_project, _board['name']))

            for _list in reversedLists:

                # 보고 완료된 'COMPLETED' 리스트를 제외
                if _list['name'] == 'COMPLETED':
                    continue
                
                # list에 card가 없는 경우 제외
                if len(card.get(_project, _board['name'], _list['name'])) == 0:
                    continue

                print("")
                print("    - " + _list['name'])

                for _card in card.get(_project, _board['name'], _list['name']):
                    
                    duedate = ""

                    if _card['item']['dueDate'] != None:
                        duedate = " (" + _card['item']['dueDate'][5:7] + "/" + _card['item']['dueDate'][8:10] + ")"

                    print("")
                    print("        - " + _card['item']['name'] + duedate)

                    for _task in task.get(_project, _board['name'], _list['name'], _card['item']['name']):
                        
                        complete = ""

                        if (_task['isCompleted']):
                            complete = "[완료] "

                        print("            - " + complete + _task['name'])




