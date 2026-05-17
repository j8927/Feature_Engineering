# ML Feature Engineering Pipeline Project

## 1. 프로젝트 개요
본 프로젝트는 Titanic Dataset을 활용하여 결측치 처리, 범주형 인코딩, 스케일링, 파생 변수 생성, 변수 선택 전략에 따른 머신러닝 성능 차이를 비교·분석하는 과제용 프로젝트입니다.

## 2. 사용 데이터셋
- Dataset: Titanic Dataset
- Task: 생존 여부 예측 Classification
- Target: `Survived`
- 조건 충족: 수치형 + 범주형 변수 포함, 결측치 포함, 500개 이상 샘플 포함

## 3. 폴더 구조
```text
ml_feature_engineering_project/
├── data/                     # 데이터 저장 위치
├── notebooks/                # 실습용 Jupyter Notebook
├── src/                      # 기능별 Python 코드
├── results/
│   ├── figures/              # EDA/성능 시각화 이미지
│   └── metrics/              # 성능 결과 CSV
├── report/                   # 보고서 템플릿
├── main.py                   # 전체 실행 파일
├── requirements.txt
├── README.md
└── .gitignore
```

## 4. 실행 방법
### 4-1. 가상환경 생성
```bash
python -m venv .venv
```

### 4-2. 가상환경 활성화
Windows PowerShell:
```bash
.venv\Scripts\Activate.ps1
```

CMD:
```bash
.venv\Scripts\activate.bat
```

macOS/Linux:
```bash
source .venv/bin/activate
```

### 4-3. 라이브러리 설치
```bash
pip install -r requirements.txt
```

### 4-4. 전체 실험 실행
```bash
python main.py
```

실행 후 다음 파일이 생성됩니다.

```text
results/figures/
results/metrics/experiment_results.csv
results/metrics/gridsearch_result.csv
results/metrics/missing_ratio.csv
```

## 5. 실험 구성
| 실험 | 결측치 처리 | 인코딩 | 스케일링 | Feature Selection |
|---|---|---|---|---|
| Base | 없음 | 없음 | 없음 | 없음 |
| Exp-1 | Mean | One-Hot | StandardScaler | X |
| Exp-2 | Median | Label/Ordinal | MinMaxScaler | O |
| Exp-3 | Most Frequent | One-Hot | RobustScaler | O |

## 6. 사용 모델
- Logistic Regression
- Random Forest Classifier

## 7. 생성 파생 변수
- `FamilySize`: 가족 수
- `IsAlone`: 혼자 탑승 여부
- `FarePerPerson`: 1인당 요금
- `AgeGroup`: 연령대
- `Title`: 이름에서 추출한 호칭

## 8. 평가 지표
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

## 9. 가산점 요소
- scikit-learn Pipeline 객체 활용
- ColumnTransformer 활용
- GridSearchCV 적용
- Feature Selection 적용
- Feature Importance/성능 시각화 가능

## 10. GitHub 제출 방법
```bash
git init
git add .
git commit -m "Initial ML feature engineering project"
git branch -M main
git remote add origin 본인깃허브주소
git push -u origin main
```

