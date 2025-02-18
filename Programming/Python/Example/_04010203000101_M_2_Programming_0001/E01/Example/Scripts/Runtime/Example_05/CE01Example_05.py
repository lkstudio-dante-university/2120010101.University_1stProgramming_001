import os
import sys


# Example 5
class CE01Example_05:
	# 초기화
	@classmethod
	def Start(cls, argv):
		# cls.E05_01(argv)
		cls.E05_02(argv)
	
	# 5 - 1
	@classmethod
	def E05_01(cls, argv):
		"""
		Python 의 자료형은 값 형식 자로형과 참조 형식 자료형으로 나뉜다. (즉, 클래스는 참조 형식 자료형에 해당하기 때문에 해당 변수에는 생성 된 
		객체가 아닌 해당 객체를 가리키는 참조 값이 할당 된다는 것을 알 수 있다.)

		값 형식 vs 참조 형식
		- 값 형식은 실제 데이터를 다루기 때문에 해당 형식 변수를 다른 변수에 할당했을 경우 사본 변수가 만들어지는 특징이 존재한다. (즉, 사본
		변수를 변경해도 원본 변수는 전혀 영향을 받지 않는다.)

		반면, 참조 형식은 실제 데이터가 아닌 해당 데이터를 가리키는 참조 값 (메모리 주소) 를 다루기 때문에 해당 형식 변수를 다른 변수에
		할당했을 경우 얕은 복사가 이루어지기 때문에 사본 변수를 변경하면 원본 변수도 영향을 받는다는 차이점이 존재한다.

		Python 값 형식 자료형
		- int
		- float

		Python 참조 형식 자료형
		- str
		- list
		- dict
		- 등등...

		즉, int 및 float 자료형을 제외하면 모두 참조 형식 자료형에 속한다는 것을 알 수 있다.
		"""
		oSuperA = CE05Super()
		oSuperB = CE05Super()
		
		"""
		객체 하위에 존재하는 멤버에 접근하기 위해서는 . (멤버 접근 연산자) 를 사용하면 된다. (즉, 해당 연산자를 활용하면 특정 객체 하위에
		존재하는 변수 및 메서드를 사용하는 것이 가능하다.
		"""
		oSuperA.m_nVal = 10
		oSuperB.m_nVal = 20
		
		print("=====> 클래스 정보 <=====")
		oSuperA.ShowInfo()
		oSuperB.ShowInfo()
	
	# 5 - 2
	@classmethod
	def E05_02(cls, argv):
		oSuper = CE05Super()
		oSub = CE05Sub()
		
		oSuper.m_nVal = 10
		
		"""
		Sub 클래스 객체는 Super 클래스를 상속했기 때문에 Sub 클래스에 있는 멤버 뿐만 아니라 Super 클래스에 존재하는 멤버도 사용 가능하다는
		것을 알 수 있다.
		"""
		oSub.m_nVal = 20
		oSub.m_oStr = "Hello, World!"
		
		print("=====> 부모 클래스 정보 <=====")
		oSuper.ShowInfo()
		
		print("\n=====> 자식 클래스 정보 <=====")
		oSub.ShowInfo()


# 부모 클래스
class CE05Super:
	"""
	생성자란?
	- 객체가 생성 될 때 Python 인터프리터에 의해서 가장 먼저 호출되는 메서드를 의미한다.
	따라서, 해당 메서드를 활용하면 객체가 동작하는데 필요한 멤버 변수를 선언하거나 객체를 초기화하는 것이 가능하다.

	Pytyon 에서 __ (더블 언더 스코어) 로 시작하는 변수나 메서드는 특별한 역할을 지니고 있기 때문에 어떤 변수나 메서드가 있는지 알아두는
	것을 추천한다.

	self 란?
	- Python 의 모든 멤버 메서드는 가장 첫번째 매개 변수로 self 를 전달받는다.

	self 란 호출 된 메서드를 지니고 있는 객체를 의미하며 해당 매개 변수를 통해 객체가 지니고 있는 멤버 변수 및 멤버 메서드에 접근하는 것이
	가능하다. (즉, 객체 내부에 존재하는 다른 멤버에 접근하기 위해서는 항상 self 키워드를 명시해줘야한다는 것을 알 수 있다.)

	또한, self 는 단순한 매개 변수 이름이기 때문에 다른 이름을 사용하는 것도 가능하지만 일반적으로 self 라고 지칭하는 것이 암묵적인 관례이다.
	"""
	
	# 생성자
	def __init__(self):
		self.m_nVal = 0
	
	# 정보를 출력한다
	def ShowInfo(self):
		print("부모 클래스 : {0}".format(self.m_nVal))


"""
Python 은 클래스 이름 뒤에 특정 클래스를 명시함으로서 명시 된 클래스를 상속하는 것이 가능하다. (즉, 특정 클래스를 상속함으로서 부모/자식의
관계가 형성된다는 것을 알 수 있다.)
"""


# 자식 클래스
class CE05Sub(CE05Super):
	# 생성자
	def __init__(self):
		"""
		super 메서드는 부모 클래스 객체를 가져오는 역할을 수행한다.
		따라서, 해당 메서드를 이용한 동일한 이름을 지닌 부모 클래스 객체의 메서드를 호출하는 것이 가능하다.

		또한, 일반적으로 객체가 정상적으로 동작하기 위해서는 해당 객체를 초기화 시켜주는 역할을 수행하는 생성자를 호출해야하기 때문에
		자식 클래스 객체의 생성자에서는 부모 클래스 객체의 생성자를 호출해주는 습관을 들이는 것이 좋다. (즉, 부모 클래스 객체의 생성자를
		따로 호출하지 않으면 해당 객체를 초기화하는 과정이 생략되어 버릴 수 있다느 것을 의미한다.)
		"""
		super().__init__()
		self.m_oStr = ""
	
	"""
	자식 클래스가 부모 클래스와 동일한 이름의 메서드를 지니고 있을 경우 우선 순위에 의해서 자식 클래스의 메서드가 호출되며 이러한 현상을
	오버라이드가 되었다고 표현한다. (즉, 자식 클래스에 존재하는 메서드가 부모 클래스에 있는 메서드를 가림으로서 부모 클래스에 존재하는
	메서드가 아닌 자식 클래스에 있는 메서드가 호출된다는 것을 의미한다.)
	"""
	
	# 정보를 출력한다
	def ShowInfo(self):
		super().ShowInfo()
		print("자식 클래스 : {0}".format(self.m_oStr))
