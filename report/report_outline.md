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
본 프로젝트는 체계적인 조합별 실험을 수행하여 전처리 전략 효과를 검증합니다.

### 기본 실험
| 실험 | 결측치 처리 | 인코딩 | 스케일링 | Feature Selection |
|---|---|---|---|---|
| Base | 없음 | 없음 | 없음 | 없음 |

### Mean Imputation 조합 (6가지)
| 실험 | 결측치 처리 | 인코딩 | 스케일링 | Feature Selection |
|---|---|---|---|---|
| Exp-1 | Mean | One-Hot | Standard | X |
| Exp-2 | Mean | One-Hot | Standard | O |
| Exp-3 | Mean | Label | Standard | X |
| Exp-4 | Mean | Label | Standard | O |
| Exp-5 | Mean | One-Hot | MinMax | X |
| Exp-6 | Mean | Label | MinMax | O |

### Median Imputation 조합 (6가지)
| 실험 | 결측치 처리 | 인코딩 | 스케일링 | Feature Selection |
|---|---|---|---|---|
| Exp-7 | Median | One-Hot | MinMax | X |
| Exp-8 | Median | One-Hot | MinMax | O |
| Exp-9 | Median | Label | MinMax | X |
| Exp-10 | Median | Label | MinMax | O |
| Exp-11 | Median | One-Hot | Robust | X |
| Exp-12 | Median | Label | Robust | O |

### Most Frequent Imputation 조합 (6가지)
| 실험 | 결측치 처리 | 인코딩 | 스케일링 | Feature Selection |
|---|---|---|---|---|
| Exp-13 | Most Frequent | One-Hot | Robust | X |
| Exp-14 | Most Frequent | One-Hot | Robust | O |
| Exp-15 | Most Frequent | Label | Robust | X |
| Exp-16 | Most Frequent | Label | Robust | O |
| Exp-17 | Most Frequent | One-Hot | Standard | X |
| Exp-18 | Most Frequent | Label | MinMax | O |

**총 실험 수**: Base 1개 + Exp-1~18 (18개) × 2 모델 = 38개 결과

## 7. 모델 학습 및 평가
- 모델: Logistic Regression, Random Forest
- 평가 지표: Accuracy, Precision, Recall, F1-score, ROC-AUC
- 각 실험 조합별 성능 비교 차트 및 분석
- 최고 성능 조합 식별 및 하이퍼파라미터 최적화 (GridSearchCV)

## 8. 변수 선택 및 Feature Importance
- SelectKBest 기반 Feature Selection 수행
- Feature Selection 적용 전/후 성능 비교
- Feature Importance 시각화 및 분석
- 중요도 상위 N개 변수 선정

## 9. 결론
- 가장 효과적인 전처리 전략 식별
- One-Hot Encoding vs Label Encoding 성능 비교 분석
- Feature Selection의 과적합 감소 기여도
- 스케일링이 모델별로 미친 영향 분석
- 결측치 처리 방법별 성능 차이
- Feature Engineering이 베이스라인 대비 성능 향상에 미친 기여도

## 10. 추가 가산점 요소
- scikit-learn Pipeline 객체 활용
- ColumnTransformer 기반 전처리
- GridSearchCV를 통한 하이퍼파라미터 최적화
- 실험별 성능 시각화 고도화
