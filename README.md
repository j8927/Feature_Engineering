# ML Feature Engineering Pipeline Project

## 1. 과제 개요
본 프로젝트는 Titanic Dataset을 활용하여 머신러닝 성능 향상을 위한 특성 공학(Feature Engineering) 파이프라인을 구현하고, 전처리 및 변수 선택 전략에 따라 성능 차이를 비교·분석합니다.

### 목표
- 데이터 탐색(EDA)부터 결측치 처리, 인코딩, 스케일링, 파생 변수 생성, 변수 선택, 모델 학습 및 평가까지 전체 ML Pipeline 구현
- 서로 다른 전처리 전략에 따른 모델 성능 비교
- 결과를 바탕으로 최적의 Feature Engineering 전략 도출

## 2. 데이터셋 소개
- Dataset: Titanic Dataset
- 과제 유형: Classification
- 목적: 생존 여부 예측 (`Survived`)
- 특성: 수치형 + 범주형 혼합, 결측치 포함, 500개 이상 샘플
- 데이터 로드: `data/titanic.csv`가 없으면 공개 GitHub 미러에서 자동 다운로드

## 3. 과제 구성
### STEP 01. 데이터 준비
- 데이터 로드 및 기본 구조 확인
- 타겟 변수 정의: `Survived`
- 데이터셋 소개 및 컬럼 설명

### STEP 02. 탐색적 데이터 분석 (EDA)
- 결측치 비율 분석
- 이상치 탐색
- 변수 분포 시각화
- 상관관계 분석
- 타겟 분포 확인

### STEP 03. 특성 공학 파이프라인 구현
- 결측치 처리 비교: Mean / Median / Most Frequent / 없음
- 범주형 인코딩 비교: One-Hot / Label
- 스케일링 비교: StandardScaler / MinMaxScaler / RobustScaler
- 파생 변수 생성: `FamilySize`, `IsAlone`, `FarePerPerson`, `AgeGroup`, `Title`

### STEP 04. 변수 선택 (Feature Selection)
- SelectKBest 적용
- 선택 전/후 성능 비교

### STEP 05. 모델 학습 및 평가
- 사용 모델: Logistic Regression, Random Forest
- 평가 지표: Accuracy, Precision, Recall, F1-score, ROC-AUC

## 4. 프로젝트 구조
```text
.
├── data/                     # 데이터 저장 위치
├── notebooks/                # Jupyter Notebook
├── report/                   # 보고서 템플릿 및 목차
├── results/
│   ├── figures/              # EDA 및 성능 시각화
│   └── metrics/              # 결과 CSV
├── src/                      # 분석 코드
├── main.py                   # 전체 실행 파일
├── requirements.txt
├── README.md
└── .gitignore
```

## 5. 실행 방법
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## 6. 출력 결과
- `results/metrics/missing_ratio.csv` : 결측치 비율 분석
- `results/metrics/experiment_results.csv` : 실험별 모델 성능 비교
- `results/metrics/gridsearch_result.csv` : GridSearchCV 최적 하이퍼파라미터
- `results/figures/` : EDA 및 성능 시각화 이미지

## 7. 실험 설계
| 실험 | 결측치 처리 | 인코딩 | 스케일링 | Feature Selection |
|---|---|---|---|---|
| Base | 없음 | 없음 | 없음 | 없음 |
| Exp-1 | Mean | One-Hot | StandardScaler | X |
| Exp-2 | Median | Label | MinMaxScaler | O |
| Exp-3 | Most Frequent | One-Hot | RobustScaler | O |

## 8. 생성된 파생 변수
- `FamilySize` : `SibSp + Parch + 1`
- `IsAlone` : 가족 없이 혼자인 경우
- `FarePerPerson` : `Fare / FamilySize`
- `AgeGroup` : 연령대 범주화
- `Title` : 이름에서 추출한 호칭

## 9. 평가 지표
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

## 10. 가산점 요소
- `sklearn.Pipeline` 객체 활용
- `ColumnTransformer` 기반 전처리
- `GridSearchCV` 적용
- 시각화 기반 비교 분석

## 11. 보고서 작성 안내
- 데이터셋 소개
- EDA 결과
- Feature Engineering 과정
- 모델 학습 및 평가
- 실험 비교 표
- 최종 결론

## 12. GitHub 제출 방법
```bash
git init
git add .
git commit -m "Initial ML feature engineering project"
git branch -M main
git remote add origin 본인깃허브주소
git push -u origin main
```
