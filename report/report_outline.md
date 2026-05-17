# 머신러닝 Feature Engineering 파이프라인 보고서 목차

## 1. 데이터셋 소개
- 데이터셋명: Titanic Dataset
- 분석 목적: 승객의 생존 여부 예측
- 타겟 변수: Survived
- 데이터 크기: 코드 실행 결과의 shape 작성

## 2. 컬럼 설명 표
| 컬럼명 | 설명 | 변수 유형 |
|---|---|---|
| PassengerId | 승객 ID | 식별자 |
| Survived | 생존 여부 | 타겟 |
| Pclass | 객실 등급 | 수치/순서형 |
| Name | 이름 | 문자열 |
| Sex | 성별 | 범주형 |
| Age | 나이 | 수치형 |
| SibSp | 형제/배우자 수 | 수치형 |
| Parch | 부모/자녀 수 | 수치형 |
| Ticket | 티켓 번호 | 문자열 |
| Fare | 운임 | 수치형 |
| Cabin | 객실 번호 | 범주형/문자열 |
| Embarked | 승선 항구 | 범주형 |

## 3. EDA 결과
- 결측치 비율 분석
- 이상치 탐색
- 변수 분포 시각화
- 상관관계 분석
- 타겟 변수 분포 확인

## 4. Feature Engineering 과정
- FamilySize
- IsAlone
- FarePerPerson
- AgeGroup
- Title

## 5. 실험 설계
| 실험 | 결측치 처리 | 인코딩 | 스케일링 | Feature Selection |
|---|---|---|---|---|
| Base | 없음 | 없음 | 없음 | 없음 |
| Exp-1 | Mean | One-Hot | Standard | X |
| Exp-2 | Median | Label/Ordinal | MinMax | O |
| Exp-3 | Most Frequent | One-Hot | Robust | O |

## 6. 모델 학습 및 평가
- Logistic Regression
- Random Forest
- Accuracy, Precision, Recall, F1, ROC-AUC 비교

## 7. 최종 결론
- 가장 효과적인 전처리 전략
- 인코딩 방식별 차이
- Feature Selection 전/후 차이
- 스케일링이 모델별로 미친 영향
- Feature Engineering의 성능 향상 기여도
