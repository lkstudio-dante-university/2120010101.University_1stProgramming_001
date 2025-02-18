using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.AI;

namespace Example
{
	/** 몬스터 */
	public class CE01Monster_23 : CE01Interactable_23
	{
		#region 변수
		private bool m_bIsDirtyUpdateUIsState = false;
		private CE01StatHandler_23 m_oStatHandler = null;

		[SerializeField] private float m_fAttackRange = 0.0f;
		[SerializeField] private float m_fTrackingRange = 0.0f;

#if UNITY_EDITOR
		[SerializeField] private string m_oCurState = string.Empty;
#endif // #if UNITY_EDITOR

		[Header("=====> UIs <=====")]
		[SerializeField] private Image m_oGaugeImg = null;
		[SerializeField] private GameObject m_oCanvas = null;
		#endregion // 변수

		#region 프로퍼티
		public float AttackRange => m_fAttackRange;
		public float TrackingRange => m_fTrackingRange;

		public Animator Animator { get; private set; } = null;
		public NavMeshAgent NavMeshAgent { get; private set; } = null;
		public CE01State_23Machine StateMachine { get; } = new CE01State_23Machine();

		public CE01StatHandler_23 StatHandler => m_oStatHandler;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake()
		{
			base.Awake();
			this.StateMachine.SetOwner(this);

			this.Animator = this.GetComponent<Animator>();
			this.NavMeshAgent = this.GetComponent<NavMeshAgent>();

			m_oStatHandler = this.gameObject.AddComponent<CE01StatHandler_23>();
		}

		/** 초기화 */
		public virtual void Init()
		{
			m_oStatHandler.SetStat(EE01StatKinds_23.HP, 5);
			m_oStatHandler.SetStat(EE01StatKinds_23.ATK, 10);
			m_oStatHandler.SetStat(EE01StatKinds_23.MAX_HP, 5);

			m_bIsDirtyUpdateUIsState = true;
			this.StateMachine.SetState(this.CreateIdleState());
		}

		/** 상태를 갱신한다 */
		public override void Update()
		{
			base.Update();
			var oSceneManager = CSceneManager.GetSceneManager<CE01Example_23>(KDefine.G_N_SCENE_EXAMPLE_23);

			// 게임 종료 상태 일 경우
			if(oSceneManager.IsGameOver())
			{
				return;
			}

			this.StateMachine.OnUpdate(Time.deltaTime);

			// UI 상태 갱신이 필요 할 경우
			if(m_bIsDirtyUpdateUIsState)
			{
				this.UpdateUIsState();
				m_bIsDirtyUpdateUIsState = false;
			}
		}

		/** 타격 되었을 경우 */
		public override void OnHit()
		{
			// 타격 가능 할 경우
			if(!m_oStatHandler.IsDie())
			{
				m_oStatHandler.IncrStatVal(EE01StatKinds_23.HP, -1);
				m_bIsDirtyUpdateUIsState = true;

				// 사망했을 경우
				if(m_oStatHandler.IsDie())
				{
					this.StateMachine.SetState(this.CreateDieState());
				}
				else
				{
					this.StateMachine.SetState(this.CreateHitState());
				}
			}
		}

		/** UI 상태를 갱신한다 */
		private void UpdateUIsState()
		{
			// 객체를 갱신한다
			m_oCanvas.SetActive(!m_oStatHandler.IsDie());

			// 이미지를 갱신한다
			m_oGaugeImg.fillAmount = m_oStatHandler.GetStatValPercent(EE01StatKinds_23.HP,
				EE01StatKinds_23.MAX_HP);
		}
		#endregion // 함수

		#region 접근 함수
		/** 공격 상태 여부를 검사한다 */
		public bool IsAttack()
		{
			return this.StateMachine.State is CE01MonsterAttackState_23;
		}

#if UNITY_EDITOR
		/** 현재 상태를 변경한다 */
		public void SetCurState(string a_oState)
		{
			m_oCurState = a_oState;
		}
#endif // #if UNITY_EDITOR
		#endregion // 접근 함수

		#region 팩토리 함수
		/** 대기 상태를 생성한다 */
		public CE01MonsterIdleState_23 CreateIdleState()
		{
			return this.CreateState<CE01MonsterIdleState_23>();
		}

		/** 추적 상태를 생성한다 */
		public CE01MonsterTrackingState_23 CreateTrackingState()
		{
			return this.CreateState<CE01MonsterTrackingState_23>();
		}

		/** 공격 상태를 생성한다 */
		public CE01MonsterAttackState_23 CreateAttackState()
		{
			return this.CreateState<CE01MonsterAttackState_23>();
		}

		/** 타격 상태를 생성한다 */
		public CE01MonsterHitState_23 CreateHitState()
		{
			return this.CreateState<CE01MonsterHitState_23>();
		}

		/** 죽음 상태를 생성한다 */
		public CE01MonsterDieState_23 CreateDieState()
		{
			return this.CreateState<CE01MonsterDieState_23>();
		}

		/** 상태를 생성한다 */
		private T CreateState<T>() where T : class, new()
		{
			var oSceneManager = CSceneManager.GetSceneManager<CE01Example_23>(KDefine.G_N_SCENE_EXAMPLE_23);

			return oSceneManager.ObjsPoolManager.SpawnObj<T>(() =>
			{
				return new T();
			}) as T;
		}
		#endregion // 팩토리 함수
	}
}
