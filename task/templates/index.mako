<!DOCTYPE html>
<html>
<head>
    <title>Results</title>
</head>
<body>
    <h1>Results</h1>
    <table>
        <thead>
            <tr>
                % for column in results[0].__table__.columns:
                <th>${column.name}</th>
                % endfor
            </tr>
        </thead>
        <tbody>
            % for result in results:
            <tr>
                % for column in result.__table__.columns:
                <td>${getattr(result, column.name)}</td>
                % endfor
            </tr>
            % endfor
        </tbody>
    </table>
</body>
</html>