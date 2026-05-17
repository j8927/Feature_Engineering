# 머신러닝 Feature Engineering 파이프라인 보고서 목차

## 1. 과제 개요
- 과제 목적: 특성 공학 기반 머신러닝 파이프라인 설계 및 성능 비교
- 선택 데이터셋: Titanic Dataset
- 학습 목표: 생존 여부 예측

## 2. 데이터셋 소개
- 데이터 출처: Titanic Dataset
- 샘플 수: 891개
- 타겟 변수: `Survived`
- 주요 특성: 수치형 + 범주형 혼합, 결측치 포함

## 3. 컬럼 설명
| 컬럼명 | 설명 | 변수 유형 |
|---|---|---|
| PassengerId | 승객 ID | 식별자 |
| Survived | 생존 여부 | 타겟 |
| Pclass | 객실 등급 | 범주형/순서형 |
| Name | 승객 이름 | 문자열 |
| Sex | 성별 | 범주형 |
| Age | 나이 | 수치형 |
| SibSp | 형제/배우자 수 | 수치형 |
| Parch | 부모/자녀 수 | 수치형 |
| Ticket | 티켓 번호 | 문자열 |
| Fare | 운임 | 수치형 |
| Cabin | 객실 번호 | 범주형/문자열 |
| Embarked | 승선 항구 | 범주형 |

## 4. EDA 결과
- 결측치 비율 분석 및 결과 해석
- 이상치 탐색 및 주요 변수 분포 분석
- 히스토그램, 박스플롯, 히트맵, 카운트플롯, 바플롯 시각화
- 타겟 변수(`Survived`) 분포 확인

## 5. Feature Engineering 과정
- 결측치 처리 전략 비교: 없음, Mean, Median, Most Frequent
- 범주형 인코딩 비교: One-Hot Encoding, Label Encoding
- 스케일링 비교: StandardScaler, MinMaxScaler, RobustScaler
- 파생 변수 생성
  - `FamilySize`
  - `IsAlone`
  - `FarePerPerson`
  - `AgeGroup`
  - `Title`

## 6. 실험 설계 및 비교
| 실험 | 결측치 처리 | 인코딩 | 스케일링 | Feature Selection |
|---|---|---|---|---|
| Base | 없음 | 없음 | 없음 | 없음 |
| Exp-1 | Mean | One-Hot | StandardScaler | X |
| Exp-2 | Median | Label | MinMaxScaler | O |
| Exp-3 | Most Frequent | One-Hot | RobustScaler | O |

## 7. 변수 선택
- SelectKBest 기반 Feature Selection 수행
- 선택 전/후 성능 비교
- 중요 변수 분석

## 8. 모델 학습 및 평가
- 모델: Logistic Regression, Random Forest
- 평가 지표: Accuracy, Precision, Recall, F1-score, ROC-AUC
- 결과 비교 차트 및 분석

## 9. 결론
- 최적 전처리 조합 도출
- One-Hot Encoding vs Label Encoding 비교
- Feature Selection의 영향
- 스케일링 효과 및 모델별 차이
- Feature Engineering의 성능 향상 기여도

## 10. 추가 가산점 요소
- Pipeline 객체 기반 전처리 구현
- ColumnTransformer 사용
- GridSearchCV 적용
- 시각화 결과 중심 분석
