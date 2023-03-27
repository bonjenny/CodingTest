class Node {
      constructor(element){
          this.element = element;
          this.prev = null;
          this.next = null;
          this.count = 0;
          this.dicPath = 0;
      }
  }

  class LinkedList {
      constructor() {
          this.head = new Node("head");
      }
    
      insert(newElement, item) {
          let newNode = new Node(newElement); //새로운 노드 생성
          let current = this.find(item); // 삽입할 위치의 노드 찾기
          newNode.next = current.next; // 찾은 노드가 가리키는 노드를 새로은 노드가 가리키기
          current.next = newNode; // 찾은 노드는 이제부터 새로운 노드를 가리키도록 하기
      }

      find(item){
          let currNode = this.head;
          while (currNode.element !== item) {
              currNode = currNode.next;
          }
          return currNode;
      }

      toString() {
          let array = [];
          let currNode = this.head;
          while(currNode.next !== null){
              array.push(currNode.next.element);
              currNode = currNode.next;
          }
          return array;
      }
  }
