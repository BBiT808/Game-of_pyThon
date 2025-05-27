        const obj = {};
        obj.a = 1;
        obj.b = 2;
        obj["c"] = function () {
            return this.b;  //여기 안에 있는 b를 보여줘 !!
        };
        obj.d = function(){
            console.log(this.a);
        };

        /* 객체의 속성과 메소드 호출 */
        console.log(obj);
        console.log(obj.c());
        obj.d();

        /* 삭제 */
        delete obj.e;
        console.log(obj);

        /* this 확인 !! */
        function test() {
            console.log(this.document);
        }
        test();

        function test2() {
            return this;
        }

        console.log(test2());