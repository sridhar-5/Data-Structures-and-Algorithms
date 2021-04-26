#include <iostream>
#include <iomanip>
using namespace std;

template <class T>
class Calculator
{
private:
        T num1, num2;

public:
        Calculator(T n1, T n2)
        {
            num1 = n1;
            num2 = n2;
        }

        void displayResult(char op)
        {
		std::cout << std::setprecision(2)<< std::fixed;;
                int val;
                //cout << "Numbers are: " << num1 << " and " << num2 << "." << endl;
                if(op == 'A')
                        cout <<  add() << endl;
                else if(op =='S')
                        cout <<  setprecision(2) << subtract() << endl;
                else if(op == 'M')
                        cout <<  multiply() << endl;
                else if(op == 'D')
                        cout <<  divide() << endl;
                else
                        cout << "Invalid operator"<<endl;
        }

        T add(){
          return num1 + num2;
        }
        T subtract(){
          return num1 - num2;
        }
        T divide(){
          return num1/num2;
        }
        T multiply(){
          return num1*num2;
        }
};

int main()
{
        int testcases;
        char operation;
        //cout << "Enter number of operation";
        cin >> testcases;
        while (testcases > 0)
        {
                float f1, f2;
                cin >> f1;
                //cout<<"Hello1"<<endl;
                cin >> f2;
                cin >> operation;
                Calculator<float> floatCalc(f1, f2);
                floatCalc.displayResult(operation);
                testcases--;
        }
        return 0;
}
